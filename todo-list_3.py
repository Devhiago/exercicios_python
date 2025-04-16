import time

# 🧙 Bem-vindo ao sistema de tarefas do Hiago!
print("🧙 Bem-vindo ao sistema de tarefas do Hiago!")

tarefas = []  # Lista que guarda as tarefas

#Escolha uma opção:
#1 - Adicionar tarefa
#2 - Ver tarefas
#3 - Remover tarefa
#4 - Sair
print("Escolha uma opção:")
print("1 - Adicionar tarefa")
print("2 - Ver tarefas")
print("3 - Remover tarefa")
print("4 - Sair")

#>>> 1
#Adicionar nova tarefa
def adicionar_tarefas(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!\n")


#>>> 2
#Tarefas:
#1. Comprar ração

def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nTarefas:")
    for i, t in enumerate(lista,0):
        print(f"{i+1}. {t}")
    print("Fim da lista de tarefas.\n")    

#>>> 3
#Digite o número da tarefa a remover: 1

def remover_tarefa(lista):
    print("Digite o número da tarefa a remover: ", end="")
    if not lista:
        print("Nenhuma tarefa encontrada.")
        return
    listar_tarefas(lista)
    try:
        index = int(input()) - 1
        if 0 <= index < len(lista):
            tarefa_removida = lista.pop(index)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!\n")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
#Tarefa removida com sucesso!

#>>> 4
#Encerrando o sistema... Até logo, Dev H-Byte!
def executar_programa():
        while True:
            opcao = input("Escolha uma opção (1-4): ")
            if opcao == "1":
                adicionar_tarefas(tarefas)
            elif opcao == "2":
                listar_tarefas(tarefas)
            elif opcao == "3":
                remover_tarefa(tarefas)
            elif opcao == "4":
                print("finalizando aplicações ...")
                time.sleep(3)
                print("Encerrando tarefas...")
                time.sleep(2.5)
                print("Encerrando o sistema de tarefas...")
                time.sleep(2)
                print("desligando as luzes...")
                time.sleep(1.5)
                print("desligando o ar condicionado...")
                time.sleep(1)
                print("desligando o computador...")
                time.sleep(0.5)
                print("Encerrando o sistema... Até logo, Dev H-Byte!")
                break
            else:
                print("Opção inválida. Tente novamente.")
                
executar_programa()