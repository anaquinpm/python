# Contributing Guide

This document defines the conventions and directory layout used to organize Python notes, exercises, and projects in this repository.

## Directory Layout

```
python/
├── README.md               # Master index of topics and projects
├── CONTRIBUTING.md         # Document structure and standards
├── notes/                  # Restructured notes folders prefixed by category number
│   ├── 01_setup/
│   │   ├── environment.md
│   │   └── packages.md
│   └── 02_fundamentals/
│       ├── basics.md
│       ├── control_flow.md
│       └── examples/       # Companion code snippets for the topic area
└── hands-on/               # Practice projects, logs, and hands-on repositories
```

## Documentation Conventions

### 1. File and Directory Naming
- Use **lowercase `snake_case`** for all markdown and code file names.
- Folders under `notes/` should be prefixed with double digits `NN_` to maintain logical reading/learning order.
- Move runnable companion scripts to the `examples/` subdirectory inside each category folder.

### 2. Frontmatter Metadata
Each note file `.md` must begin with YAML frontmatter to track status, tag topics, and cite sources:

```markdown
---
title: Topic Name
tags: [tag1, tag2]
status: complete        # options: draft | in-progress | complete
source: Ref source (e.g., Book name, URL)
last_updated: YYYY-MM-DD
---
```

### 3. Separation of Concerns
- Keep `.md` documentation clear, conceptual, and concise.
- Reference companion code scripts from the Markdown note via relative links:
  `*See companion code: [my_script.py](examples/my_script.py)*`
- Put actual runnable exercises in `examples/` rather than embedding large, raw script code block outputs in the note.

---

## Managing External Repositories (`hands-on/`)

When working with external/third-party projects under the `hands-on/` directory, use one of the two strategies below to manage them without committing foreign `.git` trees directly into this repository.

### Option A: Ignored Local Repositories (Recommended for temporary practice)

Use this method to clone repositories purely for local play and testing without pushing them to your remote.

#### 1. Download/Clone
```bash
cd hands-on/
git clone <repository_url> <directory_name>
```

#### 2. Prevent Tracking
Add the directory path to [.gitignore](.gitignore):
```gitignore
hands-on/<directory_name>/
```
*If the repository was already accidentally tracked by Git, clear it from the cache:*
```bash
git rm --cached -r hands-on/<directory_name>
```

#### 3. Delete/Remove
```bash
rm -rf hands-on/<directory_name>
```

---

### Option B: Git Submodules (Recommended for referencing active projects)

Use this method if you want to reference a specific commit of another repository on your remote without committing its source files directly.

#### 1. Add Submodule
```bash
git submodule add <repository_url> hands-on/<directory_name>
git commit -m "Add submodule hands-on/<directory_name>"
```

#### 2. Clone/Restore Submodules (For new checkouts)
If cloning this repository on a new machine or restoring submodules:
```bash
# Clone parent along with all submodules
git clone --recursive <parent_repo_url>

# Or if already cloned, initialize and update
git submodule update --init --recursive
```

#### 3. Delete/Remove Submodule
To cleanly uninstall a submodule:
```bash
# 1. De-initialize the submodule to clear config settings
git submodule deinit -f hands-on/<directory_name>

# 2. Remove the directory from Git's index and working tree
git rm -f hands-on/<directory_name>

# 3. Delete the internal Git submodule directory cache
rm -rf .git/modules/hands-on/<directory_name>
```

