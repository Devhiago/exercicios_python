#exercicio de revisão nº 1
#O programa ira imprimir uma mensagem de boas vindas e depois solicitar os 5 nomes
#Depois o usuario podera consultar os nomes e quando ele digitar "sair" o programa ira encerrar


lista = []
print("Bem vindo ao programa de cadastro de nomes!")
def cadastro():
    for i in range(5):
        nome = input(f"\nDigite o {i+1}º nome: ")
        lista.append(nome)
        print("**"*17)
        print("*  NOME CADASTRADO COM SUCESSO   *")
        print("**"*17)
        
    
def consulta():
    while True:
        nome = input("Digite um nome para consultar ou 'sair' para encerrar: ")
        if nome == "sair":
            print("Programa encerrado.")
            break
        elif nome in lista:
            print(f"O nome {nome} está na lista.")
        else:
            print(f"O nome {nome} não está na lista.")

def menu():
    print("1 - Cadastrar nomes")
    print("2 - Consultar nomes")
    print("3 - Sair") 
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número.")
        return
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consulta()
    elif opcao == 3:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")
        
def executar():
    while True:
        menu()
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != "s":
            print("Programa encerrado.")
            break
executar()