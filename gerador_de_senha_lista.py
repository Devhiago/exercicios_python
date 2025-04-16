import time
import random

keys = []
caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+"


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
    if not keys:
        print("nenhuma senha encontrada.")
    else:
        print("\nSenhas:")
        for i, t in enumerate(keys,0):
            print(f"{i+1}. {t}")
            print("Fim da lista de senhas.\n")
            time.sleep(1)
            print("senhas listadas com sucesso!\n")

