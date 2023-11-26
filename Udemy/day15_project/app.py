
agua = 300
leite = 200
cafe = 100
saldo = 0


def relatorio():
    print(f"Água: {agua}ml\nLeite: {leite}ml\n Café: {cafe}g\n Saldo: ${saldo}")


def verificar_recurso(tipo_cafe):
    global agua 
    global leite 
    global cafe 
    global saldo 

    print(tipo_cafe)
    if tipo_cafe == 'espresso': 
        if agua >= 50 and cafe >= 18:
            agua -= 50            
            cafe -= 18
            processar_moedas(tipo_cafe)
            return  True, tipo_cafe
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
            agua -= 250            
            cafe -= 24
            leite -= 100
            return  True
        else:
            return False 
     
    

def processar_moedas(tipo_cafe):
    global saldo   
    cafe = tipo_cafe

    
    print("Insira as moedas por favor")
    um = input("Quantas moedas de R$ 1.00: ")
    ciquenta = input("Quantas moedas de R$0.50: ")        
    vinte_cinco = input("Quantas moedas de R$25: ")

    total_moedas = float(um) * 1 + float(ciquenta) * 0.50 + float(vinte_cinco) * 0.25    
    processar_pagamento(total_moedas, cafe)

    return total_moedas 

def processar_pagamento(pagamento, tipo_cafe):
    global saldo
    if tipo_cafe == 'espresso':
        if pagamento > 1.50:
            print("Fazendo cafe")
            troco = pagamento - 1.5
            print(f"Seu troco: {troco}")
            saldo = 1.5
        elif pagamento == 1.50:
            print("Fazendo cafe")
            saldo = 1.5
        else:
            print("Saldo insuficiente")




def fazer_cafe():
    pass


on_off = False
while on_off != True:
    solicitacao = input("O que você gostaria? (espresso/latte/cappuccino):")
    if solicitacao == 'off':
        on_off = True
        break

    if solicitacao == 'relatorio':
        relatorio()
    else:
        verificar_recurso(solicitacao)
        

    
    
    



