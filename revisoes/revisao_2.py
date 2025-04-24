#criar um sistema de notas para alunos
#O programa ira solicitar o nome do aluno e depois as 3 notas
#o programa ira calcular a media e depois ira imprimir o nome do aluno e a media

alunos = {
    f"aluno{i}": {
        "nome": "",
        "notas": []
    } for i in range(1, 6) 
}

def cadastrar_aluno():
    for i in range(1, 6):
        nome = input(f"Digite o nome do aluno {i}: ")
        notas = []
        for j in range(1, 4):
            nota = float(input(f"Digite a nota {j} do aluno {i}: "))
            notas.append(nota)
        alunos[f"aluno{i}"]["nome"] = nome
        alunos[f"aluno{i}"]["notas"] = notas
        print("**"*17)
        print("*  ALUNO CADASTRADO COM SUCESSO   *")
        print("**"*17)

def media(notas):
    return sum(notas) / len(notas)

def consulta():
    while True:
        nome = input("Digite o nome do aluno para consultar ou 'sair' para encerrar: ")
        if nome == "sair":
            print("Programa encerrado.")
            break
        for aluno in alunos.values():
            if aluno["nome"] == nome:
                media_aluno = media(aluno["notas"])
                print(f"O aluno {nome} tem a média {media_aluno:.2f}.")
                break
        else:
            print(f"O aluno {nome} não está cadastrado.")
def menu():
    print("1 - Cadastrar alunos")
    print("2 - Consultar alunos")
    print("3 - Sair") 
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número.")
        return
    if opcao == 1:
        cadastrar_aluno()
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