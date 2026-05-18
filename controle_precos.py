preco = []

for i in range(5):
    num = float(input("Digite o valor do produto: "))

    preco.append(num)

print(f"Maior número {max(preco):.2f}")
print(f"Menor número {min(preco):.2f}")