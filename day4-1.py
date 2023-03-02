# programa que pega um nome aleatorio da lista
import random

nomes_string = input("Digite o nome dos integrantes que vão pagar a conta: ")

nomes = nomes_string.split(", ")

n = len(nomes)

num_lista = random.randint(0, n)

print(num_lista)

print(nomes[num_lista])


# mesmo programa agora com a função choice do random

