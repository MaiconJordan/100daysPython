#Função para receber nome e sobrenome de forma uniforme não importado como o imput é feito

print("Digite seu Nome e Sobrenome")
nome_completo = input()



def nome_uniforme(nome):
    nome_quebrado  = nome.split()
    for nome in nome_quebrado:
     return print(nome_completo.title())


nome_uniforme(nome_completo)




