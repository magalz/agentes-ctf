# ⚙️ Guia de Instalação e Configuração

Configurar o **CTF Professor** é um processo automatizado, mas requer alguns pré-requisitos fundamentais no seu computador.

## 🛠️ Pré-requisitos (No seu Computador Host)

Antes de começar, certifique-se de ter instalado:

1.  **Gemini CLI**: Ferramenta principal de interação. Instale via npm: `npm install -g @google/gemini-cli`.
2.  **Docker**: Essencial para rodar o sandbox Kali Linux.
3.  **Python 3.8+** e **Git**.

---

## 🚀 Método 1: Gemini CLI (Recomendado)

O **Gemini CLI** oferece a experiência mais pura e rápida. Ele detecta automaticamente a pasta `.agent/` e carrega todos os agentes e comandos.

1. Clone o repositório: `git clone https://github.com/magalz/agentes-ctf.git`
2. Entre na pasta: `cd agentes-ctf`
3. Execute o Gemini: `gemini`
4. Dentro do chat, rode a configuração automática: `/install`

---

## 🎨 Método 2: Antigravity IDE (Visual)

Se você prefere uma interface gráfica tipo VS Code, o [Antigravity IDE](https://antigravity.google) também suporta nativamente este projeto. Basta abrir a pasta e os comandos de barra estarão disponíveis no painel de chat.

### O que o `/install` faz automaticamente?

1.  **Sonda o Ambiente**: Verifica se Docker, Python e Git estão acessíveis.
2.  **Configura o Sandbox Kali**: Constrói (Build) a imagem Docker `cyber-ctf-kali` a partir do `Dockerfile` local. Esta imagem contém todas as ferramentas de segurança pré-configuradas.
3.  **Instala Dependências Python**: Instala bibliotecas como `mcp` (para comunicação IA-Sandbox), `pwntools` e `requests`.
4.  **Valida o Sistema**: Roda scripts de verificação para garantir que a IA consegue dar comandos ao container.

---

## 🐳 Entendendo a Separação Host vs. Sandbox

O sistema foi desenhado para manter seu PC limpo.

- **Host (Seu PC)**: Fica apenas com os scripts leves de Python que servem como o "Cérebro" do sistema.
- **Sandbox (Docker)**: É o "Braço" técnico. Todas as ferramentas pesadas (`nmap`, `gdb`, `wireshark`, etc.) ficam presas dentro do container, isoladas do seu sistema principal.

### Caso ocorra erros no Docker

Se o comando `/install` falhar no passo do Docker, verifique:
- Se o Docker está rodando: `docker ps`.
- No Windows: Use WSL2 como backend do Docker Desktop.
- No Linux: Adicione seu usuário ao grupo docker: `sudo usermod -aG docker $USER`.

---

## ✅ Próximo Passo

Com o ambiente configurado, você está pronto para o seu primeiro desafio. 
👉 [**Aprenda a Usar os Comandos**](Como-Usar)
