import logging
import os
from cryptography.fernet import Fernet
from app.crypto_engine import CryptoEngine

# 1. Configuração de Log (Auditoria)
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(
    filename='logs/auditoria.log',
    level=logging.INFO,
    format='%(asctime)s | %(message)s'
)

def obter_chave():
    """Lê a chave do arquivo ou cria uma nova se não existir."""
    nome_arquivo = "secret.key"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "rb") as f:
            return f.read().decode()
    else:
        # Gera uma chave válida automaticamente
        nova_chave = Fernet.generate_key().decode()
        with open(nome_arquivo, "w") as f:
            f.write(nova_chave)
        return nova_chave

def iniciar_sistema():
    chave = obter_chave()
    engine = CryptoEngine(chave)
    
    print("\n--- SafeVault TOTVS Edition ---")
    dado = input("Digite o dado sensível (ex: CPF): ")
    
    # Processamento
    token = engine.criptografar(dado)
    logging.info(f"Dado protegido. Token: {token[:15]}...")
    
    print(f"\n[PROTEGIDO NO BANCO]: {token}")
    
    input("\nPressione Enter para ver o dado original (Descriptografar)...")
    original = engine.descriptografar(token)
    print(f"[DADO ORIGINAL]: {original}")
    logging.info("Acesso autorizado ao dado original.")

if __name__ == "__main__":
    iniciar_sistema()