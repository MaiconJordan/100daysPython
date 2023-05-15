frase = input("Digite qualquer fase: ")

tam = len(frase)

metade_string = frase[:int(tam/2)]

print(metade_string[:-2:])