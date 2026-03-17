# Política de Segurança e Ética (Security & Ethics) 🎓🛡️

Este documento define as diretrizes de segurança, ética e conduta para o uso do **CTF Professor**. Ao utilizar esta ferramenta, você concorda em seguir os princípios do **Hacking Ético**.

---

## 🇧🇷 Português Brasileiro

### 🛡️ 1. Código de Conduta do Hacker Ético

O CTF Professor foi criado exclusivamente para **Educação e Pesquisa de Segurança**. O uso das técnicas e ferramentas aqui descritas em sistemas sem autorização explícita é **ilegal e antiético**.

1.  **Autorização Explícita**: Nunca utilize o sistema para analisar ou atacar alvos (IPs, domínios, binários) que não sejam de sua propriedade ou que você não tenha permissão formal para testar (ex: plataformas de CTF como HTB, TryHackMe, CTFd).
2.  **Não-Maleficência**: Suas ações não devem causar interrupções de serviço, perda de dados ou danos permanentes a sistemas de terceiros.
3.  **Privacidade e Confidencialidade**: Se você encontrar dados sensíveis durante um desafio, trate-os com o máximo sigilo. Nunca compartilhe informações privadas obtidas através de vulnerabilidades.
4.  **Divulgação Responsável**: Caso encontre uma vulnerabilidade em um sistema real, siga o processo de *Responsible Disclosure*, informando os proprietários antes de tornar a falha pública.

### 🐳 2. Segurança do Ambiente (Sandbox)

Para proteger seu computador principal (Host), o CTF Professor utiliza um **Sandbox Docker (Kali Linux)**.

-   **Isolamento**: Sempre prefira executar binários suspeitos e ferramentas de scan (`nmap`, `sqlmap`, exploits) dentro do container.
-   **Volumes**: Lembre-se que a pasta do projeto é montada como um volume. Arquivos maliciosos escritos no diretório `/workspace` dentro do container aparecerão no seu host. **Tenha cautela.**
-   **Rede**: O container tem acesso à rede para desafios remotos, mas está em uma rede `bridge` isolada da sua rede local (LAN).

### 🔑 3. Gestão de Credenciais e Segredos

O sistema de agentes é instruído a proteger segredos, mas a responsabilidade final é do usuário:
-   **Nunca** coloque chaves de API, senhas reais ou tokens no `README.md` ou em arquivos que serão commitados no Git.
-   Use arquivos `.env` e certifique-se de que eles estão no `.gitignore`.
-   Ao usar o `/start-ctf` com arquivos que contenham segredos, lembre-se que a IA processará esses dados.

### 🚩 4. Reportando Vulnerabilidades no Projeto

Se você encontrar uma falha de segurança no próprio **CTF Professor** (ex: um bypass nos guardrails dos agentes ou um problema no sandbox), por favor, reporte via:

📧 **Email**: [magalz@duck.com](mailto:magalz@duck.com)

---

## 🇺🇸 English

### 🛡️ 1. Ethical Hacker Code of Conduct

CTF Professor is created strictly for **Education and Security Research**. Using the techniques and tools described here on systems without explicit authorization is **illegal and unethical**.

1.  **Explicit Authorization**: Never use the system to analyze or attack targets (IPs, domains, binaries) that you do not own or have formal permission to test (e.g., CTF platforms like HTB, TryHackMe, CTFd).
2.  **Non-Maleficence**: Your actions must not cause service disruptions, data loss, or permanent damage to third-party systems.
3.  **Privacy and Confidentiality**: If you encounter sensitive data during a challenge, treat it with the utmost secrecy. Never share private information obtained through vulnerabilities.
4.  **Responsible Disclosure**: If you find a vulnerability in a real system, follow the *Responsible Disclosure* process, informing the owners before making the flaw public.

### 🐳 2. Environment Security (Sandbox)

To protect your main computer (Host), CTF Professor utilizes a **Docker Sandbox (Kali Linux)**.

-   **Isolation**: Always prefer executing suspicious binaries and scanning tools (`nmap`, `sqlmap`, exploits) inside the container.
-   **Volumes**: Remember that the project folder is mounted as a volume. Malicious files written to the `/workspace` directory inside the container will appear on your host. **Exercise caution.**
-   **Networking**: The container has network access for remote challenges but is on a `bridge` network isolated from your local network (LAN).

### 🔑 3. Credential & Secret Management

The agent system is instructed to protect secrets, but the ultimate responsibility lies with the user:
-   **Never** place API keys, real passwords, or tokens in the `README.md` or files that will be committed to Git.
-   Use `.env` files and ensure they are in your `.gitignore`.
-   When using `/start-ctf` with files containing secrets, remember that the AI will process this data.

### 🚩 4. Reporting Project Vulnerabilities

If you find a security flaw in **CTF Professor** itself (e.g., a bypass in agent guardrails or a sandbox issue), please report it via:

📧 **Email**: [magalz@duck.com](mailto:magalz@duck.com)

---

**Isenção de Responsabilidade (Disclaimer):** O autor do projeto não se responsabiliza pelo uso indevido desta ferramenta. O conhecimento deve ser usado para construir um mundo digital mais seguro.
**Disclaimer:** The project author is not responsible for any misuse of this tool. Knowledge should be used to build a safer digital world.
