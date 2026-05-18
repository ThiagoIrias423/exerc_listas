convidados = []

for convidado in range(5):
    nome = input('Digite o nome do convidado: ')
    convidados.append(nome)

    print(f'Foram registrados {len(convidados)} convidados')

for i in convidados:
    print(i)