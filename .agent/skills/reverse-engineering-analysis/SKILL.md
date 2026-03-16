---
name: reverse-engineering-analysis
description: Systematic RE methodology for CTF challenges. Covers static analysis, disassembly, decompilation, and pedagogical commentary on assembly. Supports ELF, PE, Mach-O, and bytecode targets.
allowed-tools: Read, Bash, Glob, Python
---

# Reverse Engineering Analysis

> Read the code the machine reads before you try to understand what it does.

---

## 1. The RE Analysis Pipeline

Follow this sequence. Never skip static analysis to jump to dynamic.

### Phase A: File Identification & Surface Analysis

1. Run `file <binary>` to identify format (ELF/PE/Mach-O/script)
2. Run `strings <binary>` to extract readable content — look for:
   - Hardcoded strings, passwords, flag formats
   - Library names and function references
   - Error messages (golden clues for logic flow)
3. Run `checksec <binary>` (for ELF) to identify protections
4. **Pedagogical Action:** Explain what each protection means and how it affects analysis

### Phase B: Static Disassembly

1. Load into **Ghidra** or use `radare2 -A` / `objdump -d`
2. Identify the entry point and trace call flow
3. Focus on:
   - `main()` function — overall program logic
   - Input handling functions (`scanf`, `fgets`, `read`, `recv`)
   - Comparison functions — where does the program check user input?
   - String construction — is the expected input built at runtime?
4. **Pedagogical Action:** Walk through each instruction block explaining:
   - What the instruction does (e.g., `mov rdi, rsp` — "moves the stack pointer into the first argument register")
   - Why it matters for the challenge
   - What a developer would need to change to fix the flaw

### Phase C: Decompilation

1. Use Ghidra's decompiler to get pseudo-C
2. Map decompiled code to assembly for accuracy verification
3. Identify the core logic:
   - What is the expected input?
   - What transformation is applied?
   - Where does the check happen?
4. **Pedagogical Action:** Ask the student to explain the decompiled logic before providing hints

### Phase D: Dynamic Analysis (When Static Is Insufficient)

1. Run under `GDB` with `pwndbg` or `GEF`
2. Set breakpoints at key comparison points
3. Trace register/memory state through the check function
4. **Rule:** Only use dynamic analysis after exhausting static — explain why

---

## 2. Architecture-Specific Notes

| Architecture | Key Registers | Common Patterns |
|:---|:---|:---|
| **x86-64** | `rdi, rsi, rdx` (args), `rax` (return), `rsp` (stack) | `call`, `cmp`, `jne/je` for checks |
| **x86-32** | Arguments on stack, `eax` (return) | `push` args before `call` |
| **ARM** | `r0-r3` (args), `lr` (return addr) | `bl` for calls, `cmp` + `beq/bne` |
| **MIPS** | `$a0-$a3` (args), `$v0` (return) | `jal` for calls, `beq/bne` branches |

---

## 3. Common RE Challenge Patterns

| Pattern | Description | Approach |
|:---|:---|:---|
| **Serial/Keygen** | Input is validated character by character | Extract comparison values from disassembly |
| **Custom Encoding** | Input is XOR'd/rotated/substituted then compared | Reverse the transformation |
| **Anti-Debugging** | `ptrace`, timing checks, environment detection | Identify and patch/bypass checks |
| **VM/Custom Bytecode** | Custom interpreter executes bytecode | Map opcode table, disassemble the bytecode |
| **Packed/Obfuscated** | UPX, custom packers, control flow obfuscation | Unpack first, then analyze |

---

## 4. Tool Reference

| Tool | Purpose | Key Commands |
|:---|:---|:---|
| `file` | Identify binary type | `file binary` |
| `strings` | Extract readable strings | `strings -n 6 binary` |
| `checksec` | Security protections | `checksec binary` |
| `readelf` | ELF structure | `readelf -h binary`, `readelf -S binary` |
| `objdump` | Quick disassembly | `objdump -d -M intel binary` |
| **Ghidra** | Full decompilation | Load → Auto-analyze → Navigate to `main` |
| `radare2` | CLI analysis | `r2 -A binary`, then `afl`, `pdf @main` |
| `GDB` | Dynamic debugging | `gdb binary`, `b main`, `r`, `ni`, `si` |
| `ltrace` | Library call tracing | `ltrace ./binary` |
| `strace` | System call tracing | `strace ./binary` |

---

## 5. Bilingual Pedagogical Prompts

### PT-BR
- "O que a função `main` faz antes de solicitar entrada do usuário?"
- "Observe a instrução `cmp`. Que valor está sendo comparado? O que isso nos diz?"
- "Antes de usar um debugger, o que podemos descobrir apenas lendo o disassembly?"

### EN
- "What does the `main` function do before asking for user input?"
- "Look at the `cmp` instruction. What value is being compared? What does this tell us?"
- "Before using a debugger, what can we discover just from reading the disassembly?"

---

## 6. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Jump straight to dynamic analysis | Exhaust static analysis first |
| Run the binary without examining it | Always `file` + `strings` + `checksec` first |
| Give the flag from `strings` output | Point the student to the anomaly and ask what it represents |
| Skip assembly explanation | Every instruction block gets pedagogical commentary |
