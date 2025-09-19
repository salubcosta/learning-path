tarefas = [] # iniciando lista de tarefas geral

def adicionar_tarefa(tarefas, nome):
    # tarefa: nome da tarefa
    # completada: indicar se essa tarefa já foi completada ou não
    tarefa = {"tarefa": nome, "completada": False }
    tarefas.append(tarefa)
    print(f"A tarefa {nome} foi adicionada ✅")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas")
    for key, item in enumerate(tarefas):
        status = "✅" if item['completada'] else "🔄️"
        print(f"Tarefa {(key+1)}: {item['tarefa']} - Status: {status}")

def atualizar_nome_tarefas(tarefas, indice, novo_nome):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["tarefa"] = novo_nome
        print(f"Tarefa {indice} atualizada para {novo_nome}")
    else:
        print("Índice de tarefa inválido!")

def completar_tarefa(tarefas, indice):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["completada"] = True
        print(f"Tarefa {indice} completada com sucesso!")
    else:
        print("Índice de tarefa inválida!")

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas")


while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Informe a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Informe o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice = input("Informe o número da tarefa: ")
        nome = input("Informe novo nome da tarefa: ")
        atualizar_nome_tarefas(tarefas, indice, nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice = input("Informe o número da tarefa que deseja finalizar: ")
        completar_tarefa(tarefas, indice)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break
    else:
        print("Opção inválida ❌")

print("Programa finalizado.2")