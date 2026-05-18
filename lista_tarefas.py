tarefas = []

while True:

    tarefa = input("Adicione uma tarefa ou fim: ")

    if tarefa == "fim":
        print('Encerrando...')
        break

    tarefas.append(tarefa)

for item in tarefas:
    print(item)