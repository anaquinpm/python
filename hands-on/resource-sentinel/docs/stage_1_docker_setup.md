# Stage 1: Dockerized Dev Environment

## Related Study Material

Before you start, make sure to read:
* **[Docker Setup](../../../notes/01_setup/docker.md)**: Details on running container environments on macOS.

**Goal**: Establish a containerized workspace so that all our Python code runs against a Linux environment from day one.

## 1. Create a `docker-compose.yml`

In the root of the `resource-sentinel` project (`hands-on/resource-sentinel/`), create a file named `docker-compose.yml`:

```yaml
services:
  dev:
    image: python:3.12-slim
    volumes:
      - .:/workspace
      # Optional: To access host system metrics securely in a read-only way:
      # - /proc:/host_proc:ro 
    working_dir: /workspace
    stdin_open: true
    tty: true
```

## 2. Start the Development Container

Open your terminal, navigate to the `hands-on/resource-sentinel/` directory, and start an interactive bash session:

```bash
docker compose run --rm dev bash
```

You are now inside the container! Any file you create locally in this directory will immediately be available inside the `/workspace` directory of the container, and you can execute it safely there.

> [!TIP]
> Keep this terminal tab open. You will write your Python code in your IDE, but you will execute your code (e.g., `python script.py`) in this terminal tab.
