# Exemplo de herança
print("\nExemplo de herança")

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro("Rex")
cat = Gato("Amy")

print("\nExemplo de polimorfismo:")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # dois underlines torna o atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


print("\nExemplo de abastração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self) -> str:
        return "Carro ligado!"

    def desligar(self) -> str:
        return "Carro desligado!"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())