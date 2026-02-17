# Projeto: Cadastro de lista de compras
# Regras:
#   - Ler e exibir a lista
#   - Abrir possibilidade de adicionar novo item

class List:

    def __init__(self, name):
        self._filename = f"{name}.txt"

    def get_list(self)->list:
        list = []
        with open(self._filename, "r") as file:
            for item in file:
                list.append(item.strip())
        return list
    
    def add_item(self, new_item: str) -> bool:
        with open(self._filename, "a") as file:
            if new_item != "":
                file.write(f"{new_item}\n")
                return True
            else:
                return False


list = List("lista")
for item in list.get_list():
    print(f"- {item}")

new_item = input("Informe novo item: ")
added = list.add_item(new_item=new_item)

if added:
    print("Item adicionado com sucesso!")
else:
    print("Não foi possível adicionar novo item.")