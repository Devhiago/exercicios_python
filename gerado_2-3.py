import time
import random

keys = {}
caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+"

# Menu
print("Escolha uma opção:")
print("1 - Gerar senha")
print("2 - Listar senhas")
print("3 - Remover senha")
print("4 - Sair")

def gerar_senha(dicionario):
    titulo = input("Digite o título para a senha: ")
    tamanho = random.randint(8, 22)  
    senha = "".join(random.choice(caracters) for _ in range(tamanho))
    
    dicionario[titulo] = senha
    print(f"Sua senha foi gerada: {senha}")
    print("Senha gerada com sucesso!\n")
    time.sleep(1)

def listar_senhas(dicionario):
    if not dicionario:
        print("Nenhuma senha encontrada.")
    else:
        print("\nSenhas:")
        for titulo, senha in dicionario.items():
            print(f"{titulo}: {senha}")
        print("Fim da lista de senhas.\n")

def remover_senha(dicionario):
    if not dicionario:
        print("Nenhuma senha encontrada.")
        return
    listar_senhas(dicionario)
    titulo = input("Digite o título da senha a remover: ")
    if titulo in dicionario:
        senha_removida = dicionario.pop(titulo)
        print(f"Senha '{senha_removida}' com o título '{titulo}' removida com sucesso!\n")
    else:
        print("Título não encontrado.")

def executar_programa():
    while True:
        opcao = input("Escolha uma opção (1-4): ")
        if opcao == "1":
            gerar_senha(keys)
        elif opcao == "2":
            listar_senhas(keys)
        elif opcao == "3":
            remover_senha(keys)
        elif opcao == "4":
            print("Finalizando aplicações ...")
            time.sleep(3)
            print("Encerrando o sistema... Até logo, Dev H-Byte!")
            break
        else:
            print("Opção inválida. Tente novamente.")

executar_programa()