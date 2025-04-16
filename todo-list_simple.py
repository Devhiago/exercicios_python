tarefas = []

while True:
  resposta = input("Deseja adicionar uma nova tarefa? : (s/n) ")
  if resposta == "s":
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f" sua tarefa foi adicionada como : {tarefa}")
    print("Tarefa adicionada com sucesso!\n")
  elif resposta == "n":
    print("Verificando tarefas adicionadas...\n")
    break
print("Tarefas adicionadas:\n")
for t in tarefas:
  print(f"- {t}\n")
  print("Fim da lista de tarefas.")
  print("Fim do programa.")