---
description: Generate a comprehensive CTF writeup based on the session history or a specific local challenge folder.
---

# /writeup - Generate CTF Report

$ARGUMENTS

---

## Task

This command transitions the session from execution to documentation. It produces a pedagogical and professional CTF writeup.

### Steps:

1. **Context Aggregation**
   - **Check for Argument**: If `$ARGUMENTS` contains a folder name (e.g., `CTF01`), read `CTFs/[Folder]/notes.md` to gather the session history, description, and flag.
   - **No Argument**: If no folder is provided, scan the immediate conversation history for successful commands, identified vulnerabilities, and executed scripts.

2. **Draft Generation**
   - Orchestrate with `ctf-writeup-architect` skill.
   - Populate the appropriate template (PT-BR or EN) using the aggregated context.
   - Ensure the "Real-World Impact & Mitigation" section translates the CTF flaw into a corporate enterprise scenario.

3. **Output and Save**
   - **Present**: Show a summary or the drafted writeup to the user.
   - **Auto-Save**: If a folder was provided in Step 1, automatically create and save the full markdown report to `CTFs/[Folder]/writeup.md`.

4. **User Review (Optional)**
   - Ask for confirmation on the exact payloads used and if any manual steps performed outside the chat need to be included.

---

## Usage Examples

```
/writeup
/writeup CTF01
/writeup focus on the buffer overflow mitigation
```

---

## Before Starting

If the CTF is not yet completed and no folder is provided, clarify the scope:
- Are we writing a partial report up to our current progress, or have you captured the flag outside of this chat?
