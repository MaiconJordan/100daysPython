# QUEM TEM MAIS SEGUIDOR
import random
from insta_dados import instagram_accounts

def adversario_um():
    n = random.randint(0, 49)    
    adv = instagram_accounts[n]    
    return str(adv['nome']), str(adv['seguidores'])
    

def adversario_dois():
    n = random.randint(0, 49)    
    adv = instagram_accounts[n]    
    return str(adv['nome']), str(adv['seguidores'])


def compara(insta_um, insta_dois):

    if insta_um > insta_dois:
        return insta_um
    else:
        return insta_dois
    
tentativas = 3

while tentativas <= 3:  
    um = adversario_um()
    dois = adversario_dois()
    resultado = compara(um, dois)

    print(' '.join(um))    
    print(' '. join(dois))
    input('Quem tem mais seguidor ? ')
    print(f'Quem tem mais seguidor é: {resultado[0]} com {float(resultado[1])} seguidores\n')
    tentativas =- 1