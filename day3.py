#numero impar ou par

num = int(input('Digite um numero e direi se ele é IMPAR ou PAR'))

resultado = num % 2

if resultado == 0:
    print('Esse número é par')
else:
    print('Esse número é impar!')