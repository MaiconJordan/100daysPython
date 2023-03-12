numeros = input("Digite os numeros que você quer a média: ").split()

for n in range(0, len(numeros)):
    n += 1
soma = 0
for i in numeros:    
    num_int = int(i)
    soma += num_int
media =  soma / len(numeros)
print(round(media))
print(soma)
print(n)
#print(media)
