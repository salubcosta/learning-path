lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)

pessoa = { "nome": "Salumão", "idade": 30, "cidade": "Brasília"}

for key, value in pessoa.items():
    print(f"{key} => {value}")

# range

for x in range(10):
    print(x, end=" ")

print("\n")

for x in range(1,11):
    print(x, end=" ")

print("\n")

lista_enumerate = ["a", "b", "c"]
for key, value in enumerate(lista_enumerate):
    print(key, ":", value)

# while
contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1
