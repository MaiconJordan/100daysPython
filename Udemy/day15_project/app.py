
agua = 300
leite = 200
cafe = 100
saldo = 0


def recurso_atual():
    print(f"Água: {agua}ml\nLeite: {leite}ml\n Café: {cafe}g\n Saldo: ${saldo}")


def verificar_recurso(tipo_cafe):
    global agua 
    global leite 
    global cafe 
    global saldo 
    print(tipo_cafe)
    if tipo_cafe == 'espresso': 
        if agua >= 50 and cafe >= 18:
            return  True
        else:
            return False
    if tipo_cafe == 'latte':
        if agua >= 200 and leite >= 150 and cafe >= 24:
            agua -= 200
            leite -= 150
            cafe -= 24
            return  True
        else:
            return False
    if tipo_cafe == 'capuccino':
        if agua >= 250 and leite >= 100 and cafe >= 24:
            return  True
        else:
            return False
        
def latte():
    agua = agua - 100        
    

def processar_moedas():
    pass

def processar_pagamento():
    pass


def fazer_cafe():
    pass


on_off = False
while on_off != True:
    solicitacao = input("O que você gostaria? (espresso/latte/cappuccino):")
    if solicitacao == 'off':
        on_off = True
        break

    if solicitacao == 'relatorio':
        recurso_atual()
    else:
        verificar_recurso(solicitacao)

    
    
    



