---
title: Docker Testing Environment
tags: [setup, docker, containers, macos]
status: complete
last_updated: 2026-07-12
---

# Docker Environment Setup on macOS

This guide provides instructions to run Python tests and examples in a Docker container on macOS, mounting the repository workspace to avoid modifying the host system.

For local non-containerized environments, see [environment.md](environment.md).

## 1. Quick Interactive Shell (One-Liner)

To launch an interactive Python container with the current workspace mounted to `/workspace`:

```bash
docker run --rm -it -v "$(pwd)":/workspace -w /workspace python:3.12-slim bash
```

> [!TIP]
> On Apple Silicon (M1/M2/M3), Docker uses virtualization to run ARM64 containers natively. To force x86_64/AMD64 emulation, add the `--platform linux/amd64` flag:
> ```bash
> docker run --rm -it --platform linux/amd64 -v "$(pwd)":/workspace -w /workspace python:3.12-slim bash
> ```

---

## 2. Docker Compose Setup

For a structured and repeatable run environment, define a `docker-compose.yml` in the root of the workspace.

### `docker-compose.yml`

Create this file in the workspace root directory:

```yaml
version: '3.8'

services:
  python-env:
    image: python:3.12-slim
    volumes:
      - .:/workspace
    working_dir: /workspace
    stdin_open: true
    tty: true
```

### Running Commands via Compose

- **Start an interactive bash session**:
  ```bash
  docker compose run --rm python-env bash
  ```

- **Run a specific script directly**:
  ```bash
  docker compose run --rm python-env python hands-on/_sandbox/script.py
  ```

---

## 3. Dependency Management

If testing requires external libraries, you can build a customized development image to cache packages.

### `Dockerfile.dev`

Create this file in the workspace root directory:

```dockerfile
FROM python:3.12-slim

WORKDIR /workspace

# Install dependencies if requirements.txt exists
COPY requirements.txt* ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["bash"]
```

### Build and Run Custom Container

1. **Build the image**:
   ```bash
   docker build -t python-dev -f Dockerfile.dev .
   ```

2. **Run with local volume mount**:
   ```bash
   docker run --rm -it -v "$(pwd)":/workspace python-dev
   ```
