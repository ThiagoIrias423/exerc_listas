lista = []

print("1-Adicionar a lista\n2-Pesquisar item\n3-Remover item\n4-alterar item\n5-lista de produtos\n6-Sair")

while True:
    opcao = int(input("Digite a opção desejata: "))

    match opcao:
        case 1:
            item = input('Qual item gostaria de adicionar: ').lower()
            lista.append(item)
        case 2:
            item = input('Qual item deseja encontrar: ').lower()
            if item in lista:
                print("Este item está na lista")
            else:
                print("Esse produto não está na lista")
        case 3:
            item = input("Qual item deseja remover").lower()
            lista.remove(item)
        case 4:
            item = input("Qual item deseja alterar: ").lower()
            if item in lista:
                item2 = input("Qual será o item que irá entrar no lugar: ").lower()
                indice = lista.index(item)
                lista[indice] = item2
                print("\nItem alterado com sucesso!")
            else:
                print("\nItem não está na lista")
        case 5:
            for i in lista:
                print(i)
        case 6:
            print("\nSaindo...")
            break