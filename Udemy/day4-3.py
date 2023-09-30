import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


opcoes  = [pedra, papel, tesoura]
num_gerado = random.randint(0, 2)
escolha_maquina = opcoes[num_gerado]


escolha_jogador = input("Escolha entre - papel, pedra e tesoura: ")

if escolha_jogador == "papel":
    print(papel)
elif escolha_jogador == "pedra":
    print(pedra)
else:
    print(tesoura)

print("###### ESOCLHA DA MAQUINA ######\n")

print(escolha_maquina)

if escolha_jogador == "papel" and escolha_maquina == opcoes[0]:
    print("JOGADOR GANHOU")
elif escolha_jogador == "papel" and escolha_maquina == opcoes[1]:
    print("JOGO EMPATADO")
elif escolha_jogador == "papel" and escolha_maquina == opcoes[2]:
    print("A MAQUINA GANHOU")
elif escolha_jogador == "pedra" and escolha_maquina == opcoes[0]:
    print("JOGO EMPATADO")
elif escolha_jogador == "pedra" and escolha_maquina == opcoes[1]:
    print("MAQUINA GANHOU")
elif escolha_jogador == "pedra" and escolha_maquina == opcoes[2]:
    print("JOGADOR GANHOU")
elif escolha_jogador == "tesoura" and escolha_maquina == opcoes[0]:
    print("MAQUINA GANHOU")
elif escolha_jogador == "tesoura" and escolha_maquina == opcoes[1]:
    print("JOGADOR GANHOU")
else:
    print("JOGO EMPATADO")