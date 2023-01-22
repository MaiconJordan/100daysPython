#calculador de gorjeta
total_conta = int(input('Qual o valor total da conta?\n'))
qtd_pessoa = int(input('Vão dividir a conta em quantas pessoas?\n'))
vlr_gorjeta = int(input('Qual o valor da gorjeta? (10, 12, 15)\n'))

#calculo da porcetagem
porct = vlr_gorjeta / 100  + 1
#calculo do total da conta + a porcetagem
total = (total_conta / qtd_pessoa) * porct

print(f'O valor total para cada um mais a gorjeta é de {total:.2f}')

