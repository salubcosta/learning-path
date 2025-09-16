###########################################################
########################## Lista ##########################
###########################################################
minha_lista = [1, 2, 3, 4, 5, "string", True, False]

print("Minha lista:", minha_lista) # output: [1, 2, 3, 4, 5, "string", True, False]

print(minha_lista[0]) # output: 1

print(minha_lista[5]) # output: string

print(minha_lista[1:-1]) # output: [2, 3, 4, 5, 'string', True]

print(minha_lista[:6]) # output: [2, 3, 4, 5, 'string']

print(minha_lista[2:]) # output: [3, 4, 5, 'string', True, False]

minha_lista[0] = "python"

print(minha_lista[:]) # output: ['python', 2, 3, 4, 5, 'string', True, False]

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após adição do valor 6:", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico e empurra pra frente o valor do índice
minha_lista.insert(2,10)
print("minha_lista.insert(2,10):",minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:",elemento_removido)
print("Minha lista após o pop(3)",minha_lista)

# Método remove
minha_lista.remove(True)
print("Minha lista após removido valor True:", minha_lista)

# Método sort
lista_de_numeros = [2,1,0,6,4,1000,-1,1]
lista_de_numeros.sort()
print(lista_de_numeros)

# Método reverse ordena de forma invertida
lista_de_numeros.reverse()
print(lista_de_numeros)

###########################################################
########################## Tupla ##########################
###########################################################

minha_tupla = (1, 2, 2, 3, 4)

contagem = minha_tupla.count(2) # output: 2

indice = minha_tupla.index(3) # output: 3


###########################################################
####################### Dicionário ########################
###########################################################

pessoa = {
    "nome": "Salumão",
    "idade": 34,
    "cidade": "Brasília"
}

print(pessoa.get("nome")) # output: Salumão

print(pessoa["nome"]) # output: Salumão

pessoa["sobrenome"] = "Barbosa"

print(pessoa)

pessoa["sobrenome"] = "Barbosa da Costa"

print(pessoa)

del pessoa["sobrenome"] 

print(pessoa)

# Método keys()
chaves = list(pessoa.keys())
print("chaves do dicionário:",chaves)
print("chaves do dicionário:",chaves[0])

# Método values
valores = list(pessoa.values())
print("chaves do dicionário:",valores)
print("chaves do dicionário:",valores[0])

# Método items
itens = pessoa.items()
print("Pares chave:valor do dicionário:", itens)
