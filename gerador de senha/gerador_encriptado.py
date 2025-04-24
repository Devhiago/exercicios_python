import os
import time
import random
from cryptography.fernet import Fernet

caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+"


# Lê a chave secreta
with open("chave.key", "rb") as chave_file:
    chave = Fernet.generate_key()
    
fernet = Fernet(chave)



def gerar_senha():
    titulo = input("Digite o título para a senha: ")
    tamanho = random.randint(8, 22)
    senha = "".join(random.choice(caracters) for _ in range(tamanho))
    senha_cripto = fernet.encrypt(senha.encode())

    with open("senhas.txt", "ab") as arquivo:
        linha = f"{titulo}:".encode() + senha_cripto + b"\n"
        arquivo.write(linha)

    print(f"Sua senha foi gerada e criptografada: {senha}")
    print("Senha salva com sucesso!\n")

def listar_senhas():
    if not os.path.exists("senhas.txt"):
        print("Nenhuma senha encontrada.")
        return
    
    with open("senhas.txt", "rb") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            print("Nenhuma senha salva.")
            return
        print("\nSenhas salvas:")
        for linha in linhas:
            try:
                titulo, senha_cripto = linha.strip().split(b":", 1)
                senha = fernet.decrypt(senha_cripto).decode()
                print(f"{titulo.decode()}: {senha}")
            except Exception as e:
                print("Erro ao descriptografar:", e)

def remover_senha():
    if not os.path.exists("senhas.txt"):
        print("Nenhuma senha para remover.")
        return

    titulo_remover = input("Digite o título da senha a remover: ")

    with open("senhas.txt", "rb") as arquivo:
        linhas = arquivo.readlines()

    novas_linhas = []
    removido = False

    for linha in linhas:
        if linha.startswith(f"{titulo_remover}:".encode()):
            removido = True
            continue
        novas_linhas.append(linha)

    with open("senhas.txt", "wb") as arquivo:
        arquivo.writelines(novas_linhas)

    if removido:
        print(f"Senha com título '{titulo_remover}' removida com sucesso!")
    else:
        print("Título não encontrado.")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Gerar senha")
        print("2 - Listar senhas")
        print("3 - Remover senha")
        print("4 - Sair")

        opcao = input("Opção: ")
        if opcao == "1":
            gerar_senha()
        elif opcao == "2":
            listar_senhas()
        elif opcao == "3":
            remover_senha()
        elif opcao == "4":
            print("Encerrando o sistema... Até logo, Dev H-Byte!")
            break
        else:
            print("Opção inválida!")

menu()
