# 🛡️ SafeVault: Micro-API de Anonimização (LGPD-Ready)

Este projeto simula uma ferramenta de segurança para proteção de dados sensíveis (PII), focada em conformidade com a LGPD. Desenvolvido como prova de conceito para integração com sistemas ERP (como os da TOTVS).

## 🚀 Tecnologias e Conceitos
- **Python 3.x**: Linguagem base.
- **Cryptography (Fernet)**: Criptografia simétrica de alta segurança.
- **Modularização**: Separação clara entre lógica de negócio (`app/`) e execução (`main.py`).
- **Audit Log**: Registro de trilhas de auditoria para conformidade e segurança.
- **Git/GitHub**: Controle de versão com boas práticas de `.gitignore`.

## 🛠️ Como testar
1. Instale a biblioteca: `pip install cryptography`
2. Rode o projeto: `python main.py`
3. Verifique a pasta `logs/` para ver a trilha de auditoria criada.

---
*Projeto desenvolvido para demonstração técnica de habilidades em segurança e arquitetura de software.*
