---
title: Packages
tags: [setup, packages, pip, poetry, uv, security]
status: complete
source: General Reference
last_updated: 2026-07-20
---

# Package Management

Python packages extend the language's capabilities. Managing dependencies correctly ensures reproducible builds, prevents conflicts, and protects against supply chain attacks.

- [Search packages on PyPI](https://pypi.org)

## Virtual Environment Isolation

Always run Python projects inside a virtual environment (`venv`) to isolate dependencies from the global operating system Python installation.

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it (Unix/macOS)
source .venv/bin/activate

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

## Legacy Package Management (`pip`)

List dependencies in the current environment:

```bash
pip freeze --local
```

Generate a dependencies file (`requirements.txt`):

```bash
pip freeze --local > requirements.txt
```

### Common Pip Commands
```sh
# Install a package from PyPI
pip install requests

# Install specific version (Best Practice)
pip install requests==2.31.0

# Install from a requirements file
pip install -r requirements.txt

# Upgrade a package
pip install requests --upgrade

# Uninstall a package
pip uninstall requests
```

## Modern Packaging Tools

While `pip` is standard, modern projects use advanced dependency managers that offer deterministic lockfiles.

### 1. Poetry
`poetry` manages dependencies, virtual environments, and package builds using a single `pyproject.toml` file.
```bash
# Initialize a poetry project
poetry init

# Add a package (automatically resolves and updates pyproject.toml & poetry.lock)
poetry add requests

# Run a script inside the poetry environment
poetry run python main.py
```

### 2. UV (Rust-based packaging)
`uv` is an extremely fast, single-binary Python package installer and resolver written in Rust, designed as a drop-in replacement for `pip` and `pip-tools`.
```bash
# Install package using uv (typically 10-100x faster than pip)
uv pip install -r requirements.txt
```

## Security Best Practices

### 1. Pin Dependencies
Avoid installation of unversioned packages in production. Always pin your packages to specific versions or version ranges in your configuration to avoid breaking changes when packages upgrade.
* **Bad**: `requests`
* **Good**: `requests==2.31.0`

### 2. Vulnerability Auditing
Python packages can contain known security vulnerabilities. Use `pip-audit` to scan the environment or local requirements file against the PyPI vulnerability database.

```bash
# Install auditor
pip install pip-audit

# Audit current environment
pip-audit

# Audit a requirements.txt file
pip-audit -r requirements.txt
```

### 3. Prevent Dependency Confusion
When using private registries alongside PyPI, prioritize your internal packages or configure explicit repository sources to prevent attackers from registering public packages with your private names.
