c = []

fahrenheit = []

while True:
    temp = input("Digite uma temperatura em graus celsius 0 para sair: ")

    if temp == 'sair':
        break
    else:
        c.append(float(temp))
       
print(f'Media celsius = {sum(c) / len(c)}')

for i in c:

    f = i * 9 / 5 + 32

    fahrenheit.append(f)

print(f'Media Fahrenheit = {sum(fahrenheit) / len(fahrenheit)}')
