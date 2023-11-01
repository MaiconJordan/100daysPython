

print("\nACERTE TODAS AS UF(ESTADOS) DO BRASIL\n")

acertos = []

ufs = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

uf_jorgador = []


while True:

    uf = input("\nDIGITE UMA UF: ")  
    
    
    
    if uf.upper() in ufs and uf.upper() not in uf_jorgador: 
        uf_jorgador.append(uf.upper())
        acertos.append(uf.upper()) 
        print()
        print("ACERTOS: ", " ".join(acertos))
    else: 
        print("UF INVALIDA OU JA DIGITADA")        
   

    
    

        

