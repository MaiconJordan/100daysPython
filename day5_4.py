import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_let= int(input(f"Quantas letras você quer que tenha na senha?\n")) 
nr_sim = int(input(f"Quantos simbolos você quer que tenha na senha?\n"))
nr_num = int(input(f"Quantos números você quer que tenha na senha?\n"))

lista_senha = []

for le in range(1, nr_let+1):
    lista_senha.append(random.choice(letters))

for nr in range(1, nr_sim+1):
    lista_senha += random.choice(numbers)

for nru in range(1, nr_num+1):
    lista_senha.append(random.choice(symbols))

random.shuffle(lista_senha)
senha_pronta = ""
for l in lista_senha:
    senha_pronta += l

print(senha_pronta)