# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome):
        self.nome = nome

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para o valor={cls.valor}"

    @staticmethod
    def metodo_estatico():
        return f"Médodo estático chamado"
    
obj = MinhaClasse("oi")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao)
print(f"Marca:{carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a,b):
        return a+b
    
print(Matematica.somar(10,5))