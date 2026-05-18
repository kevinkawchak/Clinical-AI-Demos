# Authoring Instructions for `src/robot_loop.cpp`

The future session writes this C++ source during Commit 3 of 7. It is the per-robot 10 Hz motion loop with a 5 ms E-stop reaction time. Compiles under g++, clang++, and MSVC.

## Purpose

Runs inside each Unitree H2's onboard compute. Subscribes to the per-robot command topic. Runs the motion loop at 10 Hz. Reacts to E-stop messages from peers within 5 ms.

## Build Targets

- MacOS: clang++ with `-std=c++20 -O2` and the `pthread` flag.
- Linux: g++ with `-std=c++20 -O2 -pthread`.
- Windows: MSVC cl.exe with `/std:c++20 /O2`.

A shared `CMakeLists.txt` is authored in commit 4 alongside `Cargo.toml` for cross-language reproducibility.

## Key Behavior

- Subscribes to topic `site/{site_id}/robot/{robot_id}/command`.
- Maintains a 5-deep circular buffer of the most recent `humanoid_command` records.
- At every motion tick (10 Hz), interpolates between the last achieved pose and the current target pose.
- Computes inverse kinematics via the shared kinematics chain in `kinematics.yaml`.
- Drives the 39 joint controllers via the Unitree SDK interface (`unitree_sdk2`).
- Listens for `e_stop_propagation` messages on the IR beacon channel at 1000 Hz; reaction within 5 ms (1 motion tick at 200 Hz override).

## Suggested Skeleton

```
#include <atomic>
#include <chrono>
#include <cstdint>
#include <queue>
#include <thread>

namespace pat_net_001 {

struct PoseXYZ {
  double x;
  double y;
  double z;
};

struct OrientationRPY {
  double roll;
  double pitch;
  double yaw;
};

struct HumanoidCommand {
  std::string command_id;
  int64_t tick;
  std::string site;
  std::string robot_id;
  std::string role;
  PoseXYZ target_pose;
  OrientationRPY target_rpy;
  std::string gripper_state;
  std::array<std::string, 2> peer_robot_ids;
  double synergy_score;
};

class RobotLoop {
 public:
  RobotLoop(std::string robot_id) : robot_id_(std::move(robot_id)), e_stop_(false) {}

  void run() {
    auto next_tick = std::chrono::steady_clock::now();
    while (!stop_.load()) {
      if (e_stop_.load()) {
        emergency_brake();
      } else {
        motion_tick();
      }
      next_tick += std::chrono::milliseconds(100);  // 10 Hz
      std::this_thread::sleep_until(next_tick);
    }
  }

  void on_command(const HumanoidCommand& cmd) {
    std::lock_guard<std::mutex> lock(mu_);
    if (pending_.size() >= 5) pending_.pop_front();
    pending_.push_back(cmd);
  }

  void on_estop() {
    e_stop_.store(true);
  }

  void clear_estop() {
    e_stop_.store(false);
  }

  void stop() {
    stop_.store(true);
  }

 private:
  void motion_tick() {
    HumanoidCommand current;
    {
      std::lock_guard<std::mutex> lock(mu_);
      if (pending_.empty()) return;
      current = pending_.back();
    }
    auto joint_targets = inverse_kinematics(current.target_pose, current.target_rpy);
    drive_joints(joint_targets);
  }

  void emergency_brake() {
    // halt all 39 joints, latch into safe pose, hold for 5 seconds
  }

  std::vector<double> inverse_kinematics(const PoseXYZ& xyz, const OrientationRPY& rpy);
  void drive_joints(const std::vector<double>& targets);

  std::string robot_id_;
  std::atomic<bool> stop_{false};
  std::atomic<bool> e_stop_{false};
  std::mutex mu_;
  std::deque<HumanoidCommand> pending_;
};

}  // namespace pat_net_001
```

## Camarade Invariants Enforced Here

- E-stop propagation within 5 ms: the IR beacon listener thread spins at 1000 Hz and flips `e_stop_` immediately on any peer E-stop message.
- Joint envelope: before driving joints, the loop checks that the trajectory does not enter a peer's 2 second envelope.

## Validation Rules

- 10 Hz tick rate, 100 ms period.
- E-stop reaction time at most 5 ms.
- No dynamic memory allocation in the hot path (use the circular buffer).

## Notes

- This file is plain C++ standalone; it does not link to the Python source. Communication with the Python side is via the broadcast bus.
- Lint: clang-format default. No ruff (ruff is Python only).
- Compile under all 3 OS. CMakeLists in commit 4 makes the cross-OS build one-line.
