---
description: Analyze a binary artifact for reverse engineering or exploitation. Automatically detects whether the binary is an RE or Pwn challenge and routes to the appropriate specialist.
---

# /analyze-binary - Analyze a Binary Artifact

$ARGUMENTS

---

## Task

This command performs deep analysis on a binary file and routes to the appropriate specialist agent.

### Steps:

1. **Intake**: Identify the attached binary file.
   - If no file is attached, ask: "Attach the binary file or provide its path." / "Anexe o arquivo binario ou forneca o caminho."

2. **Initial Analysis** (automatic):
   - Run `file <binary>` to identify the format
   - Run `strings -n 6 <binary>` and scan for interesting patterns
   - Run `checksec <binary>` (if ELF) to map protections
   - Present the summary to the student

3. **Classification Decision**:
   - If a **remote connection** (nc/socat/port) is provided → Route to `binary-exploit-engineer` (Pwn)
   - If **no remote**, "crack"/"keygen" keywords → Route to `reverse-engineering-specialist` (RE)
   - If ambiguous → Ask the student: "Is there a remote service to connect to?" / "Ha um servico remoto para conectar?"

4. **Specialist Handoff**: Transfer context to the appropriate specialist agent and continue with their methodology.

---

## Usage Examples

```
/analyze-binary
/analyze-binary + attached crackme
/analyze-binary nc ctf.example.com 1337 + attached binary
/analyze-binary Binario ELF com conexao remota na porta 9999
```

---

## Rules

- **Always run file + strings + checksec before anything else.**
- **Never execute the binary blindly** — analyze first.
- **Language follows the user's input language.**
