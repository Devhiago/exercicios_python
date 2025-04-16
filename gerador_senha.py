import random

size = int(input("Quantos caracteres voce quer na sua senha? "))
caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}"
senha =""
random.choice(caracters)
for i in range(size):
  senha += random.choice(caracters)
print(f"sua senha foi gerada: {senha}")
