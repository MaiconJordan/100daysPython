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
        if insta_um[1] > insta_dois[1]:
            return insta_um
        else:
            return insta_dois
  

    

def run():
    tentativas = 3
    while tentativas > 0:  
        print(tentativas)
        um = adversario_um()
        dois = adversario_dois()
        resultado = compara(um, dois)
    
        print(um[0])    
        print(dois[0])
        esc = input('Quem tem mais seguidor ? 1 ou 2 ')
        if esc == '1':
            esc = um
        else:
            esc = dois     

        if esc == resultado:
            print('Acertou\n')
        else:
            
            print(f'Quem tem mais seguidor é: {resultado[0]} com {float(resultado[1])} seguidores\n')    
            tentativas = tentativas - 1



run()