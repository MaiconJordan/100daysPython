import random
from os import system, name

def limpa_tela():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
    pass





def rand_palavra():

    palavras = ['banana','abacate','laranja','morango']

    palavra = random.choice(palavras)

def main():
    limpa_tela()


    game = Hangman(rand_palavra())

