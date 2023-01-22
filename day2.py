#calculador de gorjeta
total_conta = int(input('Qual o valor total da conta?\n'))
qtd_pessoa = int(input('Vão dividir a conta em quantas pessoas?\n'))
vlr_gorjeta = int(input('Qual o valor da gorjeta? (10, 12, 15)\n'))

""" Meu Calculo
#calculo da porcetagem
porct = vlr_gorjeta / 100  + 1
#calculo do total da conta + a porcetagem
total = (total_conta / qtd_pessoa) * porct
"""

#calculo refatorado pela prof Angela
porct = vlr_gorjeta /100
total_gorjeta = total_conta * porct
total = total_conta + total_gorjeta
total_qtd_pessoa = total / qtd_pessoa


print(f'O valor total para cada um mais a gorjeta é de {total_qtd_pessoa:.2f}')

