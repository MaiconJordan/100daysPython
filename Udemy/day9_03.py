# Projeto leilão
import os

def limpar_tela():
    sistema_operacional = os.name

    if sistema_operacional == 'posix':  # Linux e macOS
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        # Em outros sistemas, tentamos utilizar um método alternativo
        print('\n' * 100)

# Exemplo de uso



print("\nBem vindo ao Leilão!!")
leilao = True
participantes = {}

while leilao:    
    limpar_tela()
    nome = input("Qual seu nome: ")
    lance = int(input("Qual o valor do lance: "))    
    rodada = input("Outra pessoa irá da um lance? (S / N )")

    participantes[nome] = lance

    if rodada.upper() != "S":
        leilao = False   
        chave_maior_valor = max(participantes, key=participantes.get)
        valor_maior = participantes[chave_maior_valor]     
        print(f'Quem venceu o leilão foi, {chave_maior_valor}, com o lance de R$ {float(valor_maior)}')
        
        
        


    



