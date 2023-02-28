import random

import random

nomes_string = input("Digite o nome dos integrantes que vão pagar a conta: ")

nomes = nomes_string.split(", ")


escolhe_nome = random.choice(nomes)

print(escolhe_nome)