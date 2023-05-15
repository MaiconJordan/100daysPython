preco = int(input("Digite o valor do produto: "))

desconto = int(input("Digite o valor do desconto: "))

total = preco / (desconto/100)

print(f"Valor total com desconto de {desconto}% : {total}")  