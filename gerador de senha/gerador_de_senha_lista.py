import time
import random

keys = []
caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+"

#menu
print("Escolha uma opção:")
print("1 - Gerar senha")
print("2 - Listar senhas")
print("3 - Remover senha")
print("4 - Sair")


def gerar_senha(lista):
  tamanho =  int(input("digite a quantidade de caracteres que deseja na senha: "))
  senha = ""
  for i in range(tamanho):
      senha += random.choice(caracters)
      
  print(f"sua senha foi gerada: {senha}")
  keys.append(senha)
  print("senha gerada com sucesso!\n")
  time.sleep(1)
      
def listar_senhas(lista):
    if not lista:
        print("Nenhuma Senha encontrada.")
    else:
        print("\nSenhas:")
    for i, t in enumerate(lista,0):
        print(f"{i+1}. {t}")
    print("Fim da lista de senhas.\n") 
    
def remover_senha(lista):
    print("Digite o número da senha a remover: ", end="")
    if not lista:
        print("Nenhuma senha encontrada.")
        return
    listar_senhas(lista)
    try:
        print("Listando senhas salvas\n ", end="")
        index = int(input()) - 1
        if 0 <= index < len(lista):
            senha_removida = lista.pop(index)
            print(f"Senha '{senha_removida}' removida com sucesso!\n")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        
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
                print("finalizando aplicações ...")
                time.sleep(3)
                print("Encerrando keys)...")
                time.sleep(2.5)
                print("Encerrando o sistema de keys)...")
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