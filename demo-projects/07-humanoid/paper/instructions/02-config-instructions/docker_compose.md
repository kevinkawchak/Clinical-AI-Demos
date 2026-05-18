# Authoring Instructions for `docker-compose.yml`

The future session writes this file at the root of the instruction tree during Commit 1 of 7.

## Purpose

Declares the docker services for the 4-site simulation.

## Content

```
version: "3.9"

services:
  llm-sf01:
    build: ./docker/llm
    environment:
      - SITE_ID=SF-01
      - ANTHROPIC_BASE_URL=http://anthropic-onprem:8080
    volumes:
      - ./config:/config:ro
      - ./data:/data
    networks:
      - pat-net-001

  llm-sd01:
    build: ./docker/llm
    environment:
      - SITE_ID=SD-01
      - ANTHROPIC_BASE_URL=http://anthropic-onprem:8080
    volumes:
      - ./config:/config:ro
      - ./data:/data
    networks:
      - pat-net-001

  llm-bo01:
    build: ./docker/llm
    environment:
      - SITE_ID=BO-01
      - ANTHROPIC_BASE_URL=http://anthropic-onprem:8080
    volumes:
      - ./config:/config:ro
      - ./data:/data
    networks:
      - pat-net-001

  llm-at01:
    build: ./docker/llm
    environment:
      - SITE_ID=AT-01
      - ANTHROPIC_BASE_URL=http://anthropic-onprem:8080
    volumes:
      - ./config:/config:ro
      - ./data:/data
    networks:
      - pat-net-001

  ingest:
    build: ./docker/ingest
    volumes:
      - ./data:/data
      - ./schemas:/schemas:ro
    networks:
      - pat-net-001

  simulator:
    build: ./docker/simulator
    environment:
      - ITERATION_COUNT=32
    volumes:
      - ./config:/config:ro
      - ./data:/data
    networks:
      - pat-net-001

  db:
    image: ghcr.io/duckdb/duckdb-server:latest
    volumes:
      - ./data:/data
    networks:
      - pat-net-001

  cross-site-bus:
    build: ./docker/cross-site-bus
    environment:
      - PHI_EGRESS=forbidden
    volumes:
      - ./data:/data
    networks:
      - pat-net-001

networks:
  pat-net-001:
    driver: bridge
```

## Validation Rules

- 4 per-site LLM services, 1 ingest, 1 simulator, 1 db, 1 cross-site-bus.
- All services share the `pat-net-001` bridge network.
- `PHI_EGRESS=forbidden` is set on the cross-site bus.

## Notes

- The `Dockerfile`s under `docker/` are minimal: Python 3.12 slim base, `pip install -r requirements.txt`, copy source.
- For local development the docker compose stack is optional; the Python entrypoints can run standalone.
