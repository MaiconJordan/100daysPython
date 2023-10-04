#Try Execpt

def askint():
    while True:
        try:
            val = int(input("Digite um numero: "))
        except:
            print("Você não digitou um numero")
            continue
        else:
            print("Obrigado por digitar um numero")
            break
        finally:
            print("Fim da Execução")
        print(val)


askint()