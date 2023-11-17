import random

NUMERO_ESCOLHIDO = random.randint(1, 100)
 
print("ADIVINHE O NUMERO de 1 a 100")
dificuldade = input("Qual dificuldade você quer FACIL ou DIFICIL? F / D: ")
d = dificuldade.upper()

def diff(dif):    
    if dif == "F":
        return 10
    else:
        return 5
    
def advinha_num(num):
    if num > NUMERO_ESCOLHIDO:
        return "\nO número é menor"
    elif num < NUMERO_ESCOLHIDO:        
        return "\nO numero é maior"
    else:
        return " "
 

tentativas = diff(d)

while tentativas > 0:
    numero = int(input("Escolha um número: "))
    maior_menor = advinha_num(numero)
    print(maior_menor)
    if numero == NUMERO_ESCOLHIDO:
        print("Você Acertou !")
        break

    tentativas -= 1





#dificuldade_rodada = diff(dificuldade)
#print(dificuldade_rodada)






