# Projeto: Cadastro de lista de compras
# Regras:
#   - Ler e exibir a lista
#   - Abrir possibilidade de adicionar novo item

# Exemplo estruturado

with open("lista.txt", "r") as lista:
    for item in lista:
        print(f"- {item.strip()}")

print("#"*10)

with open("lista.txt", "a") as lista:
    novo_item = input("Informe novo item: ")
    if novo_item != "":
        lista.write(f"{novo_item}\n")
        print("Item adicionado com sucesso!")
    else:
        print("Você não informou nenhum item.")
