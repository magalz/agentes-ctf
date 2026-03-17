# CTF Professor 🎓🛡️

> **Um mentor de cibersegurança que ensina você a pensar, no terminal onde o trabalho acontece.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: PT-BR](https://img.shields.io/badge/Idioma-PT--BR-009c3b)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-EN-blue)](README.md)
[![Powered by Gemini CLI](https://img.shields.io/badge/Powered%20by-Gemini%20CLI-blue)](https://github.com/google/gemini-cli)

O **CTF Professor** é um sistema de agentes de IA focado no ensino de cibersegurança através de desafios de CTF. Projetado para rodar diretamente no seu terminal via **Gemini CLI**, ele oferece uma experiência leve, poderosa e sem distrações gráficas.

---

## 🚀 Quick Start (Início Rápido via Gemini CLI)

### 1. Pré-requisitos
- **Docker** instalado e rodando.
- **Python 3.8+** e **Git**.
- **Gemini CLI** instalado (`npm install -g @google/gemini-cli`).

### 2. Instalação e Configuração
Clone o repositório e rode o instalador automático:

```bash
git clone https://github.com/magalz/agentes-ctf.git
cd agentes-ctf

# Inicie o Gemini CLI nesta pasta forçando o uso do modelo Pro (Essencial para CTFs):
gemini --model gemini-3.0-pro

# Dentro do Gemini CLI, configure o ambiente:
/install
```

### 3. Comece a Aprender
O modo recomendado de usar o CTF Professor é criando uma pasta para o seu desafio:

1.  Crie uma subpasta em `CTFs/` (ex: `CTFs/meu-pwn/`).
2.  Coloque os arquivos do desafio (binários, fontes, descrição) lá dentro.
3.  No Gemini CLI, inicie o desafio pelo nome da pasta:

```bash
/start-ctf meu-pwn
```
*(Você também pode simplesmente colar a URL de um desafio do CTFd, HackTheBox ou TryHackMe no `/start-ctf` para baixar os arquivos automaticamente!)*

**Dica de Organização:** Use o comando `/list-ctf` a qualquer momento no terminal para ver todos os seus desafios locais, a quantidade de arquivos em cada um e o status de resolução.

---

## 🌟 Recursos Destacados

- **Integração com Plataformas**: Conecte suas contas do **CTFd**, **HackTheBox** e **TryHackMe** (`/link-ctf`) para automatizar o download de desafios e envio de flags.
- **Sandbox Seguro (Docker)**: Executa ferramentas agressivas (nmap, gdb, sqlmap) dentro de um contêiner Kali Linux isolado, mantendo seu PC protegido.
- **Fluxo Pedagógico (2 Passos)**: A IA não apenas resolve; ela avalia suas respostas, corrige seus erros metodológicos e só então executa as ferramentas.
- **Geração de Writeups**: Ao final do desafio, use `/writeup` para que o sistema documente todos os passos e gere um relatório profissional com impacto corporativo (STRIDE).

---

## 🔥 Por que usar no Terminal (Gemini CLI)?

- **⚡ Performance**: Sem o overhead de interfaces gráficas pesadas.
- **🛠️ Fluxo Nativo**: Alinhado com as ferramentas que você já usa no dia a dia de segurança.
- **🧩 Extensível**: Integração perfeita com o Sandbox Docker e ferramentas locais (Notepad++, ImHex).
- **🧠 Foco Total**: Interface puramente textual que prioriza o raciocínio socrático.

---

## 📚 Documentação Completa (Wiki)

Para guias detalhados, arquitetura técnica, expectativas de custos de IA e manuais de uso, visite nossa **Wiki**:

1.  [**Home**](https://github.com/magalz/agentes-ctf/wiki/Home) - Visão geral e Filosofia Terminal-First.
2.  [**Guia de Instalação**](https://github.com/magalz/agentes-ctf/wiki/Instalacao) - Configuração via Gemini CLI e Sandbox.
3.  [**Modelos e Custos**](https://github.com/magalz/agentes-ctf/wiki/Modelos-e-Custos) - *Leitura Obrigatória*: Por que usar o modelo Pro e não o Flash.
4.  [**Ferramentas Locais**](https://github.com/magalz/agentes-ctf/wiki/Ferramentas-Locais) - Recomendações de editores de texto e hexadecimais para o Host.
5.  [**Manual de Comandos**](https://github.com/magalz/agentes-ctf/wiki/Como-Usar) - Como interagir com o Professor e listar desafios.
6.  [**Agentes e Skills**](https://github.com/magalz/agentes-ctf/wiki/Agentes-e-Skills) - Como o ecossistema técnico "pensa".
7.  [**Sandbox Kali Docker**](https://github.com/magalz/agentes-ctf/wiki/Sandbox-Docker) - Detalhes sobre segurança e o ambiente de execução.
8.  [**Contribuindo**](https://github.com/magalz/agentes-ctf/wiki/Contribuindo) - Como expandir o sistema com novas capacidades.

---

## 🤝 Créditos e Referências

O **CTF Professor** foi construído utilizando como base e inspiração os seguintes projetos:

- [vudovn/antigravity-kit](https://github.com/vudovn/antigravity-kit) - Framework base de agentes e workflows.
- [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) - Repositório original de habilidades (skills).

---

## 📄 Licença

Licença MIT - Sinta-se livre para usar, aprender e contribuir!
