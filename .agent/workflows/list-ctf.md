---
description: List all local CTF challenges stored in the CTFs/ directory.
---

# /list-ctf — Manage Local Challenges

$ARGUMENTS

---

## Task

### Step 1: Scan CTFs Directory
1. **Invoke** `.agent/scripts/list_ctfs.py`.
2. **Display** a table of challenges found in `CTFs/`.

### Step 2: Analysis
For each folder, show:
- **Name**: The subfolder name.
- **Artifacts**: Total number of files.
- **Status**: 
    - `🆕 New`: Just files, no notes.
    - `⏳ In Progress`: Contains a `notes.md` file.
    - `🏁 Solved`: Contains a file with "flag" in the name.

---

## Usage Examples

```
/list-ctf
```

---

## Rules
- **Formatting**: Present the list in a clean, readable table format.
- **Empty State**: If the directory is empty, encourage the user to create their first folder.
