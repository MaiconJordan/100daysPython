lista_pecas = []
codigo_peca = 0

# cadastro das peças
def cadastrar_peca(codigo):    
    print('Bem vindo ao menu de cadastrar Peça')
    print(f'Código da peça: {codigo}')
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    valor = float(input('Entre com o VALOR(R$) da peça: '))
    dic_peca = {'codigo': codigo,
                'nome': nome,
                'fabricante': fabricante,
                'valor':valor}
    lista_pecas.append(dic_peca.copy())
# consultar  peças
def consultar_peca():
    while True:
        print('Bem vindo ao menu de consultar Peça')    
        opcao_consultar = input('Escolha a opção desejada: \n '+
                                '1-Consultar Todas as Peças  \n'+
                                '2-Consultar Peças por Código\n'+
                                '3-Consultar peças por Fabricante\n'+
                                '4-Retornar\n >>> ' )
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar todos as Peças') 
            for peca in lista_pecas:
                for key, value in peca.items():
                    print(f'{key} : {value}')  
                print('-----' * 5)
        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar Peça por Código')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for peca in lista_pecas:
                if peca['codigo'] == valor_desejado:
                    print('-----' * 5)
                    for key, value in peca.items():
                    
                        print(f'{key} : {value}')    
                    print('-----' * 5)                  
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Peças por Fabricante')
            valor_desejado = input('Entre com o FABRICANTE desejado: ')
            for peca in lista_pecas:
                if peca['fabricante'] == valor_desejado:
                    print('-----' * 5)
                    for key, value in peca.items():
                        print(f'{key} : {value}')  
                    print('-----' * 5)
        elif opcao_consultar == '4':
            return 
        else:
            print('OPÇÃO INVALIDA, DIGITE UMA DAS OPÇÕES')
            continue

# remover das peças
def remover_peca():
    print('Bem vindo ao menu de remover Peça') 
    valor_desejado = int(input('Entre com o codigo da PEÇA que deseja REMOVER: '))
    for peca in lista_pecas:
        if valor_desejado == peca['codigo']:
            lista_pecas.remove(peca)
            print('-----------------')
            print(f'PRODUTO REMOVIDO')
            print('-----------------')
# menu
print('Bem vindo ao controle de estoque da Bicicletaria do Maicon Jordan 4497651')

while True:
    opcao_principal = input('Escolha a opção desejada: \n '+
                             '1-Cadastras Peças \n'+
                             '2-Consultar Peças\n'+
                             '3-Remover peça\n'+
                             '4-Sair\n >>> ' )
    if opcao_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrar_peca(codigo_peca)
    elif opcao_principal == '2':
        consultar_peca()
    elif opcao_principal == '3':
        remover_peca()
    elif opcao_principal == '4':
        break
    else:
        print('OPÇÃO INVALIDA, DIGITE UMA DAS OPÇÕES')
        continue