# Lista que guarda as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!\n")

# Função para mostrar todas as tarefas
def mostrar_tarefas(lista):
    print("\nTarefas adicionadas:")
    for t in lista:
        print(f"- {t}")
    print("Fim da lista de tarefas.\n")

# Função principal do programa
def executar_programa():
    while True:
        resposta = input("Deseja adicionar uma nova tarefa? (s/n) ")
        if resposta == "s":
            adicionar_tarefa(tarefas)
        elif resposta == "n":
            print("\nVerificando tarefas adicionadas...")
            mostrar_tarefas(tarefas)
            print("Fim do programa.")
            break
executar_programa()