# QUEM TEM MAIS SEGUIDOR
import random
from insta_dados import instagram_accounts

def adversario_um():
    n = random.randint(1, 51)
    adv = instagram_accounts[n]
    return adv['nome'], adv['seguidores']
    

def adversario_dois():
    n = random.randint(1, 51)
    adv = instagram_accounts[n]
    return adv['nome'], adv['seguidores']
    




um = adversario_um()

print(um)
