c = []

fahrenheit = []

while True:
    temp = float(input("Digite uma temperatura em graus celsius 0 para sair: "))

    if temp == 0:
        break
c.append(temp)

for i in c:
    print(f'Media celsius = {sum(c) / len(c)}')

f = i * 9 / 5 + 32

fahrenheit.append(f)

for ff in fahrenheit:
    print(f'Media Fahrenheit = {sum(fahrenheit) / len(fahrenheit)}')