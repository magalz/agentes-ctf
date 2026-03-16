# 🎓 CTF Professor — Cybersecurity Education Agent System

[![Status: v1.0](https://img.shields.io/badge/Version-1.0-blue.svg)](https://github.com/magalz/agentes-ctf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: PT-BR](https://img.shields.io/badge/Idioma-PT--BR-009c3b)](#pt-br)
[![Language: EN](https://img.shields.io/badge/Language-EN-blue)](#en)
[![Antigravity](https://img.shields.io/badge/Powered%20by-Antigravity-red)](https://antigravity-kit.unikorn.vn)

---

### 📑 Documentação / Documentation

- [🇧🇷 Português Brasileiro](#pt-br)
- [🇺🇸 English](#en)
- [📜 Licença / License](LICENSE)
- [🛡️ Segurança / Security](SECURITY.md)

---

<details id="pt-br-details" open>
<summary><h2 id="pt-br" style="display:inline;">🇧🇷 Português Brasileiro (Padrão)</h2></summary>

### O que é isso?

**CTF Professor** é um ambiente educacional de ciberseguranca construido sobre o framework [Antigravity Kit](https://antigravity-kit.unikorn.vn), originalmente um fork do [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills).

Diferente de ferramentas que resolvem desafios automaticamente, este sistema se comporta como um **Professor de Cibersegurança**:

- Ele **ensina**, não apenas resolve
- Ele **guia** por raciocínio estruturado
- Ele **desafia** seu pensamento com perguntas socráticas
- Ele **aplica** uma metodologia de aprendizado antes de permitir a execução
- Ele **conecta** vulnerabilidades do CTF com segurança corporativa real
- Ele **detecta automaticamente** seu idioma (EN/PT-BR) e responde adequadamente

### Filosofia Central

> *"Não ensine apenas como encontrar a flag; ensine a compreensão da vulnerabilidade que permitiu sua existência."*

### O Ciclo de Aprendizado

1.  **CLASSIFICAÇÃO** -> Taxonomia 3 níveis (Tipo/Categoria/Classe)
2.  **ANÁLISE DO CENÁRIO** -> Categorizar o desafio, formular hipóteses
3.  **RECONHECIMENTO GUIADO** -> Identificar vetores de ataque com explicações
4.  **BASE TEÓRICA** -> Compreender a vulnerabilidade antes de usar ferramentas
5.  **EXPLORAÇÃO CONTROLADA** -> Construir o exploit passo a passo com gates socráticas
6.  **CAPTURA DA FLAG** -> Validar sucesso; explicar o que a flag representa
7.  **MITIGAÇÃO E WRITEUP** -> Traduzir a falha para risco corporativo e remediação

### Sistema de Agentes (18 agentes)

| Agente | Função |
| :--- | :--- |
| `ctf-professor` | Orquestrador principal - educador socrático |
| `challenge-classifier` | Classificação 3 níveis em cada sessão |
| `reverse-engineering-specialist` | Analise binária estática-primeiro |
| `binary-exploit-engineer` | Ciclo Teoria-Prever-Executar-Verificar |
| `crypto-analyst` | Análise matemática de cifras |
| `forensics-analyst` | PCAP, memória, stego, disco |
| `malware-sandbox-analyst` | Análise segura de malware |
| `security-auditor` | Revisão de código e avaliação de vulnerabilidades |
| `penetration-tester` | Simulação de engajamento completo |

### Fluxos de Trabalho (Slash Commands)

| Comando | Propósito |
| :--- | :--- |
| `/start-ctf` | Iniciar sessão (3 modos: vazio / texto+arquivos / imagem+arquivos) |
| `/classify-challenge` | Classificação standalone de desafio |
| `/hint` | Dica progressiva 3 níveis com gate |
| `/analyze-binary` | Analise profunda de binário |
| `/explain-vulnerability` | Explicação educacional pura |
| `/threat-model` | Modelo de ameaças STRIDE pós-captura |
| `/replay-exploit` | Teste de retenção - reproduzir e explicar |

### Guia de Instalação

#### Pré-requisitos
- [Antigravity IDE](https://antigravity.im) (recomendado), [VS Code](https://code.visualstudio.com/) ou [Cursor](https://cursor.sh/)
- Git instalado e configurado
- Python 3.8+ (opcional para scripts)

#### Método 1: Antigravity IDE (Recomendado)
1.  **Instale o Antigravity IDE** em [antigravity.im](https://antigravity.im).
2.  **Clone e abra o projeto**:
    ```bash
    git clone https://github.com/magalz/agentes-ctf.git
    ```
    Abra a pasta no Antigravity: `File > Open Folder`.
3.  **Pronto!** O Antigravity detecta o diretório `.agent/` automaticamente.

#### Método 2: VS Code
1.  **Instale a extensão Gemini Code Assist**.
2.  **Abra o projeto**: O diretório `.agent/` é detectado no chat Gemini.

### Guia de Uso

```
# Exemplo de Início
/start-ctf Injeção SQL em página de login
```

O sistema guiará você por todas as fases, do reconhecimento até a flag e o writeup final.

---
</details>

<details id="en-details">
<summary><h2 id="en" style="display:inline;">🇺🇸 English</h2></summary>

### What is this?

**CTF Professor** is a cybersecurity educational environment built on the [Antigravity Kit](https://antigravity-kit.unikorn.vn).

Unlike tools that solve challenges automatically, this system behaves like a **Cybersecurity Professor**:

- It **teaches**, not just solves
- It **guides** through structured reasoning
- It **challenges** your thinking with Socratic questions
- It **auto-detects** your language (EN/PT-BR)

### Core Philosophy

> *"Do not just teach how to find the flag; teach the understanding of the vulnerability that allowed it to exist."*

### The Learning Cycle

1.  **CLASSIFICATION** -> 3-tier challenge taxonomy
2.  **SCENARIO ANALYSIS** -> Form initial hypotheses
3.  **GUIDED RECONNAISSANCE** -> Identify attack vectors
4.  **THEORETICAL FOUNDATION** -> Understand the vulnerability
5.  **CONTROLLED EXPLOITATION** -> Step-by-step with Socratic gates
6.  **FLAG ACQUISITION** -> Explain result
7.  **MITIGATION & WRITEUP** -> Translate to enterprise risk

### Agent System

| Agent | Role |
| :--- | :--- |
| `ctf-professor` | Lead orchestrator - Socratic educator |
| `challenge-classifier` | 3-tier classification on every session |
| `reverse-engineering-specialist` | assembly-level guidance |
| `binary-exploit-engineer` | Theory-Predict-Execute-Verify |
| `crypto-analyst` | Cipher identification-first |

### Workflows

| Command | Purpose |
| :--- | :--- |
| `/start-ctf` | Start the learning cycle (3 input modes) |
| `/hint` | Progressive 3-tier hint |
| `/analyze-binary` | Deep binary analysis |
| `/explain-vulnerability` | Pure educational explanation |
| `/threat-model` | Post-capture STRIDE threat model |

### Installation Guide

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/magalz/agentes-ctf.git
    ```
2.  **Open in Antigravity IDE**: The IDE will automatically load all agents and skills from the `.agent/` folder.
3.  **Start Learning**: Type `/start-ctf` to begin your first challenge.

---
</details>

---

## 📜 Creditos/Credits

| Project | Role |
|:---|:---|
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | Original Skill Repository |
| [Antigravity Kit](https://antigravity-kit.unikorn.vn) | Framework Foundation |

> **An AI agent system focused on teaching cybersecurity through CTF.**