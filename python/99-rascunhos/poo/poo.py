# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome   = nome
        self.idade  = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos
pessoa1 = Pessoa("Salumão", 34)
print(pessoa1.saudacao())

pessoa2 = Pessoa("Joelda", 32)
print(pessoa2.saudacao())