from cryptography.fernet import Fernet

class CryptoEngine:
    def __init__(self, chave: str):
        """Inicializa o motor com uma chave mestra."""
        self.f = Fernet(chave.encode())

    def criptografar(self, texto: str) -> str:
        """Transforma texto legível em um token ilegível."""
        return self.f.encrypt(texto.encode()).decode()

    def descriptografar(self, token: str) -> str:
        """Transforma o token de volta em texto legível."""
        return self.f.decrypt(token.encode()).decode()