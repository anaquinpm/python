---
title: Packages
tags: [setup, packages, pip]
status: complete
source: General Reference
last_updated: 2026-07-10
---

# Packages

- [Search packages](https://pypi.org)

## Packages Installed

Used to list dependencies installed in the current `venv` or globally.

```bash
pip3 freeze --local
```

This can be used to generate a requirements file for the project:

```bash
pip3 freeze --local > requirements.txt
```

## Different Ways to Install Packages

```sh
# Install from PyPI
pip install <myPackage>
pip install <myPackage>==<version>  # Specify a version

# Install from a requirements file
pip install -r requirements.txt

# Upgrade a package
pip install <myPackage> --upgrade
pip install <myPackage>==<version> --upgrade

# Uninstall a package
pip uninstall <package>
pip uninstall -r requirements.txt

# Install and remove packages with pip-autoremove (removes unused dependencies)
pip install pip-autoremove
pip-autoremove <package> -y

# Install from a local source directory
cd <directorySetFiles>
python3 -m pip install .

# Install directly from a Git repository
pip install git+https://github.com/your-repo.git

# Install from a compressed archive
python3 -m pip install package.tar.gz
```
