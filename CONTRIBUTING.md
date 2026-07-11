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
