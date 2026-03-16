# CTF Professor - Cybersecurity Education Agent System

> **Um sistema de agentes de IA focado em ensinar ciberseguranca atraves de CTF, nao apenas em resolver desafios.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: PT-BR](https://img.shields.io/badge/Idioma-PT--BR-009c3b)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-EN-blue)](README.md)
[![Antigravity](https://img.shields.io/badge/Powered%20by-Antigravity-red)](https://antigravity-kit.unikorn.vn)
[![Forked from](https://img.shields.io/badge/Forked%20from-sickn33%2Fantigravity--awesome--skills-lightgrey)](https://github.com/sickn33/antigravity-awesome-skills)

---

## Idioma / Language

- [Portugues Brasileiro](#portugues-brasileiro) ← *Idioma principal*
- [English](#english) ← *Primary documentation reference*

---

## Portugues Brasileiro

### O que e isso?

**CTF Professor** e um ambiente educacional de ciberseguranca construido sobre o framework [Antigravity Kit](https://antigravity-kit.unikorn.vn), originalmente um fork do [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills).

Diferente de ferramentas que resolvem desafios automaticamente, este sistema se comporta como um **Professor de Ciberseguranca**:

- Ele **ensina**, nao apenas resolve
- Ele **guia** por raciocinio estruturado
- Ele **desafia** seu pensamento com perguntas socraticas
- Ele **aplica** uma metodologia de aprendizado antes de permitir a execucao
- Ele **conecta** vulnerabilidades do CTF com seguranca corporativa real
- Ele **detecta automaticamente** seu idioma (EN/PT-BR) e responde adequadamente

### Filosofia Central

> *"Nao ensine apenas como encontrar a flag; ensine a compreensao da vulnerabilidade que permitiu sua existencia."*

### O Ciclo de Aprendizado

```
1. CLASSIFICACAO          -> Taxonomia 3 niveis (Tipo/Categoria/Classe)
2. ANALISE DO CENARIO     -> Categorizar o desafio, formular hipoteses
3. RECONHECIMENTO GUIADO  -> Identificar vetores de ataque com explicacoes
4. BASE TEORICA           -> Compreender a vulnerabilidade antes de usar ferramentas
5. EXPLORACAO CONTROLADA  -> Construir o exploit passo a passo com gates socraticas
6. CAPTURA DA FLAG        -> Validar sucesso; explicar o que a flag representa
7. MITIGACAO E WRITEUP    -> Traduzir a falha para risco corporativo e remediacao
```

### Sistema de Agentes (18 agentes)

| Agente | Funcao |
|:---|:---|
| `ctf-professor` | Orquestrador principal - educador socratico |
| `challenge-classifier` | Classificacao 3 niveis em cada sessao |
| `reverse-engineering-specialist` | Analise binaria estatica-primeiro |
| `binary-exploit-engineer` | Ciclo Teoria-Prever-Executar-Verificar |
| `crypto-analyst` | Analise matematica de cifras |
| `forensics-analyst` | PCAP, memoria, stego, disco |
| `malware-sandbox-analyst` | Analise segura de malware |
| `security-auditor` | Revisao de codigo e avaliacao de vulnerabilidades |
| `penetration-tester` | Simulacao de engajamento completo |

### Fluxos de Trabalho (Slash Commands)

| Comando | Proposito |
|:---|:---|
| `/start-ctf` | Iniciar sessao (3 modos: vazio / texto+arquivos / imagem+arquivos) |
| `/classify-challenge` | Classificacao standalone de desafio |
| `/hint` | Dica progressiva 3 niveis com gate |
| `/analyze-binary` | Analise profunda de binario |
| `/explain-vulnerability` | Explicacao educacional pura |
| `/threat-model` | Modelo de ameacas STRIDE pos-captura |
| `/replay-exploit` | Teste de retencao - reproduzir e explicar |

### Guia de Instalacao

#### Pre-requisitos

- [Antigravity IDE](https://antigravity.im) (recomendado), [VS Code](https://code.visualstudio.com/) ou [Cursor](https://cursor.sh/)
- Git instalado e configurado
- (Opcional) Python 3.8+ para o script `classify.py`
- (Opcional) Ferramentas CTF: `pwntools`, `Ghidra`, `Wireshark`, `Volatility 3`, etc. — o sistema guia voce sobre o que e necessario por desafio

#### Metodo 1: Antigravity IDE (Recomendado)

O Antigravity suporta nativamente a estrutura `.agent/`. Skills, agentes e workflows sao carregados automaticamente.

1. **Instale o Antigravity IDE** em [antigravity.im](https://antigravity.im):
   - Windows: Baixe o instalador `.exe` e execute o wizard
   - macOS: Baixe o `.dmg` e arraste para Aplicativos
   - Linux: Siga as instrucoes do gerenciador de pacotes no site

2. **Faca login** com sua conta Google no primeiro uso

3. **Clone e abra o projeto**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   ```
   Abra a pasta `agentes-ctf` no Antigravity: `File > Open Folder`

4. **Pronto!** O Antigravity detecta o diretorio `.agent/` automaticamente. Todos os 18 agentes, 28 skills e 13 workflows ficam disponiveis. Digite `/start-ctf` no chat para comecar.

#### Metodo 2: VS Code com Gemini Code Assist

1. **Instale o VS Code** em [code.visualstudio.com](https://code.visualstudio.com/)
2. **Instale a extensao Gemini Code Assist**: Extensions (`Ctrl+Shift+X`) > busque "Gemini Code Assist" > Sign in
3. **Clone e abra**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   code agentes-ctf
   ```
4. **Verifique**: Abra o painel Gemini e digite `/start-ctf` para testar.

#### Metodo 3: Integracao Manual

```bash
git clone https://github.com/magalz/agentes-ctf.git
cd agentes-ctf
# A pasta .agent/ contem tudo — aponte seu workspace aqui
```

---

### Guia de Uso

#### Iniciando uma Sessao CTF

```
# Modo A: Vazio — o sistema vai pedir detalhes
/start-ctf

# Modo B: Texto + arquivos — descreva o desafio e anexe arquivos
/start-ctf Injecao SQL em pagina de login com MySQL
# (anexe arquivos fonte ou artefatos do desafio)

# Modo C: Imagem + arquivos — anexe screenshot do desafio
/start-ctf
# (anexe screenshot + binario/arquivos fonte)
```

O sistema automaticamente:
1. Detecta seu idioma (EN ou PT-BR)
2. Invoca o `challenge-classifier` para categorizar o desafio
3. Direciona para o agente especialista apropriado
4. Inicia o ciclo de aprendizado guiado

#### Todos os Slash Commands

| Comando | O Que Faz | Exemplo |
|:---|:---|:---|
| `/start-ctf` | Iniciar sessao de aprendizado | `/start-ctf buffer overflow em binario ELF` |
| `/hint` | Dica progressiva (3 niveis) | `/hint` |
| `/classify-challenge` | Classificar sem resolver | `/classify-challenge` + anexar arquivo |
| `/analyze-binary` | Analise profunda de binario | `/analyze-binary` + anexar binario |
| `/explain-vulnerability` | Explicar qualquer vulnerabilidade | `/explain-vulnerability SSRF` |
| `/threat-model` | Modelo de ameacas apos resolver | `/threat-model` |
| `/replay-exploit` | Testar sua retencao | `/replay-exploit` |
| `/debug-exploit` | Debugar exploit falhando | `/debug-exploit` |
| `/writeup` | Gerar relatorio pedagogico | `/writeup` |

#### Exemplo de Fluxo de Sessao

```
Voce:   /start-ctf Tenho um desafio web com formulario de login
Agente: [Detecta idioma: PT-BR]
Agente: [Classificador: Web Exploitation > SQLi > Error-based]
Agente: "Vamos comecar com reconhecimento. O que voce ve quando
         visualiza o codigo-fonte da pagina?"

Voce:   Tem um formulario PHP enviando para login.php
Agente: "Otimo. Antes de usar qualquer ferramenta, tente enviar
         uma aspas simples no campo de usuario. O que acontece?"

Voce:   Apareceu um erro MySQL!
Agente: "Excelente — isso confirma SQLi error-based. Voce consegue
         explicar POR QUE o servidor mostrou esse erro?"

...     [Exploracao guiada com gates socraticas]

Voce:   Peguei a flag! FLAG{sql_1nj3ct10n_m4st3r}
Agente: "Parabens! Agora vamos entender o impacto real.
         Use /threat-model para analisar esta vulnerabilidade, ou
         /writeup para documentar o que voce aprendeu."
```

---

## Creditos

| Project | Role |
|:---|:---|
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | Repositório original de Skills |
| [Antigravity Kit](https://antigravity-kit.unikorn.vn) | Framework de Agentes/Skills/Workflows |

All upstream work retains its original MIT License. This project's CTF-specific additions are also MIT licensed.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
