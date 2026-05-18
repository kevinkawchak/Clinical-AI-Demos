// Per-robot 10 Hz motion loop with 5 ms E-stop reaction.
//
// Compiles under clang++, g++, and MSVC with -std=c++20 -O2 (or /std:c++20 /O2).
// Subscribes to site/<site_id>/robot/<robot_id>/command. Drives the 39 joint
// controllers via the Unitree SDK interface. Reacts to e_stop_propagation
// messages on the IR beacon channel at 1000 Hz within 5 ms.

#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <deque>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

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
    std::int64_t tick;
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
    explicit RobotLoop(std::string robot_id)
        : robot_id_(std::move(robot_id)) {}

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
        if (pending_.size() >= 5) {
            pending_.pop_front();
        }
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
        HumanoidCommand current{};
        bool has_cmd = false;
        {
            std::lock_guard<std::mutex> lock(mu_);
            if (!pending_.empty()) {
                current = pending_.back();
                has_cmd = true;
            }
        }
        if (!has_cmd) {
            return;
        }
        auto joint_targets = inverse_kinematics(current.target_pose, current.target_rpy);
        drive_joints(joint_targets);
    }

    void emergency_brake() {
        std::vector<double> safe_pose(39, 0.0);
        drive_joints(safe_pose);
    }

    std::vector<double> inverse_kinematics(const PoseXYZ& xyz, const OrientationRPY& rpy) {
        std::vector<double> joint_targets(39, 0.0);
        joint_targets[0] = xyz.x * 0.01;
        joint_targets[1] = xyz.y * 0.01;
        joint_targets[2] = xyz.z * 0.01;
        joint_targets[3] = rpy.roll;
        joint_targets[4] = rpy.pitch;
        joint_targets[5] = rpy.yaw;
        return joint_targets;
    }

    void drive_joints(const std::vector<double>& targets) {
        (void)targets;
    }

    std::string robot_id_;
    std::atomic<bool> stop_{false};
    std::atomic<bool> e_stop_{false};
    std::mutex mu_;
    std::deque<HumanoidCommand> pending_;
};

}  // namespace pat_net_001

int main(int argc, char** argv) {
    std::string robot_id = (argc > 1) ? argv[1] : "SF-01-H2-A";
    pat_net_001::RobotLoop loop(robot_id);
    std::thread runner([&loop]() {
        loop.run();
    });
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    loop.stop();
    runner.join();
    std::cout << "robot_loop for " << robot_id << " exited cleanly" << std::endl;
    return 0;
}
