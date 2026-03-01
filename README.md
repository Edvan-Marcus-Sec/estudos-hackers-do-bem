# 🛡️ Formação Hackers do Bem - Portfólio de Estudos
Repositório dedicado ao armazenamento de scripts, laboratórios e anotações teóricas do programa **Hackers do Bem**. Foco em Segurança da Informação, Automação e práticas de **DevSecOps**.

---

## 🚀 Módulo 5: Gerenciamento de Identidades e Contas
Neste módulo, explorei os fundamentos de **IAM (Identity and Access Management)**, desde a integração de colaboradores até protocolos avançados de autorização em nuvem.

### 📚 Resumo Teórico
* **Ciclo de Vida de Identidade:** Onboarding (integração), Gestão de Ativos, Acordos de Confidencialidade (NDA) e Offboarding (desativação segura).
* **Controles de Gerenciamento:** Uso de PKI (Certificados Digitais), Smart Cards, Tokens e Chaves SSH para autenticação forte.
* **Governança de Privilégios:** Implementação do **Menor Privilégio**, Separação de Funções (SoD) e Rotação de Cargos.
* **Modelos de Controle de Acesso:** - **DAC:** Controle Discricionário (Dono define permissão).
    - **RBAC:** Baseado em Funções/Cargos.
    - **MAC:** Obrigatório (Rótulos de Confidencialidade).
    - **ABAC:** Baseado em Atributos (Contexto).
* **Protocolos Modernos:** LDAP para diretórios, OAuth 2.0 para autorização e OpenID Connect (OIDC) para autenticação federada.

---

## 🛠️ Ferramentas e Scripts Desenvolvidos

### 1. Port Scanner Automatizado (`scanner.py`)
Script Python que realiza o reconhecimento de portas TCP abertas em um alvo.
* **Conceitos:** Redes, Sockets, Reconhecimento.
* **Uso:** `python3 scanner.py`

### 2. Validador de Políticas de Senha (`validador_senha.py`)
Automatização da verificação de conformidade de senhas baseada em regras de complexidade.
* **Conceitos:** Políticas de Segurança, Expressões Regulares (Regex).
* **Uso:** `python3 validador_senha.py`

### 3. Blindagem de Arquivos em Lote (`blindar_arquivos.py`)
Script de segurança que aplica o **Menor Privilégio** em arquivos críticos (`.txt`, `.json`, `.py`), removendo acessos de terceiros via `chmod`.
* **Conceitos:** Permissões Linux (rwx), Automação de Segurança.
* **Uso:** `python3 blindar_arquivos.py`

### 4. Modelo de Política IAM (`politica_acesso.json`)
Exemplo de "Segurança como Código" definindo permissões de leitura e bloqueio de exclusão em ambientes Cloud.
* **Conceitos:** JSON, Cloud Security, Least Privilege.

---

## 💻 Tecnologias e Lab Environment
* **OS:** Kali Linux 
* **Linguagens:** Python 3, Bash
* **Controle de Versão:** Git / GitHub
* **Metodologia:** DevSecOps (Security as Code)

---
*Estudos realizados por **Edvan Marcus** como parte da trilha de Segurança da Informação.*
