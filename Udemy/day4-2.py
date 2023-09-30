#Exercicio de listas
linha1 = ["o","o","o"]
linha2 = ["o","o","o"]
linha3 = ["o","o","o"]

quadro = [linha1 , linha2, linha3]
print("  1     2      3")
print(f"1{linha1}\n2{linha2}\n3{linha3}")

linha_escolinha = input("Veja o quadro acima, digite qual bola você quer acertar.\nutilando primeiro a coluna e depois a linha ex: 21  (coluna 2 linha 1): ")

coluna = int(linha_escolinha[0])
linha = int(linha_escolinha[1])

quadro[linha - 1][coluna - 1] = "X"


print("  1     2      3")
print(f"1{linha1}\n2{linha2}\n3{linha3}")




