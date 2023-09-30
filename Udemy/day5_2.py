#Obter o valor maximo da lista, sem a função max()
lista_de_numeros = [76, 2, 30, 40, 50, 101, 20, 35, 12, 0, 5]

n_maior = 0
for n in lista_de_numeros:
    if n > n_maior:
        n_maior = n
print(n_maior)