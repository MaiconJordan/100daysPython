#calculo de IMC com laudo 
print('=========== BEM VINDO AO CALCULO DO IMC ===========\n')


nome = input('Qual o seu nome?\n')
altura = float(input('Qual a sua altura?\n'))
peso = float(input('Qual o seu peso?\n'))

imc = peso / (altura * altura)

if imc > 18.5 and imc < 24.9:
    imc_d = 'Peso normal'
elif imc >= 25.0 and imc < 29.9:
    imc_d = 'Sobrepeso'
elif imc >= 30 and imc < 34.9:
    imc_d = 'Obesidade grau I'
elif imc >= 35 and imc < 29.9:
    imc_d = 'Obesidade grau II'
elif imc >= 40:
    imc_d = 'Obesidade mórbida'
else:
    imc_d = 'Abaixo do Peso'

print(f'Olá {nome} seu IMC é {imc:.2f} e você está com {imc_d}')
    
