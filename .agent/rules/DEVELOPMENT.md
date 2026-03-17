---
description: Context and rules for developing the tool itself (agents, rules, skills).
---

# DEVELOPMENT.md — CTF Professor Development Guidelines

> This file defines the context and rules for **modifying or extending** the CTF Professor teaching environment. 
> It should only be active when the user explicitly confirms they want to develop the tool itself.

---

## 🏗️ Structural Modification Principles

When acting as a developer of this tool, you must follow these principles:

1. **Do No Harm to the Pedagogical Flow**: Any changes to agents, skills, or rules must preserve the core Socratic and pedagogical principles of the tool. Do not break the "Read -> Understand -> Apply" loop.
2. **Modularity**: Agents and skills are highly modular. Skills should be decoupled and reusable across agents. Do not create monolithic structures.
3. **Documentation**: Any new skill, agent, or workflow MUST be thoroughly documented following the standard markdown structure with appropriate frontmatter.

## 🛠️ Modifying Core Architecture

When instructed to modify files like `ARCHITECTURE.md`, `GEMINI.md`, or the `.agent` directory structure:

- Verify the impact of the changes against existing agents.
- When creating new agents, ensure they are correctly registered in the routing tables.
- Update `ARCHITECTURE.md` if directories or major components change.

## 🧪 Testing Changes

- Structural changes should ideally be tested within a controlled context before committing.
- Ensure any added scripts in `.agent/scripts` are cross-platform or explicitly document their environment requirements.

## ⚠️ Safe Context Switching

When returning to normal CTF session work, the agent must drop this development context and revert to standard student learning constraints.
