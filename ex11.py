'''Exercicio de fila de atendimento'''
lista_clientes = ['José', 'Pedro', 'Rafael', 'Amanda']
while True:
    print('==============')
    print('1-Novo cliente')
    print('Atender cliente')
    print('==============')

    opcao = int(input('Escolher ação: '))
    if opcao == 1:
        print('Fila do Atendimento: ', lista_clientes)
        novo_cliente = input('Novo cliente: ')
        lista_clientes.append(novo_cliente)
        print('Fila do Atendimento: ', lista_clientes)
        print('Cadastrado com sucesso!')
    if opcao == 2:
        for cliente in lista_clientes:
            while True:
                print('Atendendo ', cliente)
                flag = int(input('Digite ZERO para encerrar o atendimento'))
                print('Fila do Atendimento: ', lista_clientes)
                if flag == 0:
                    del(lista_clientes[0])
                    print('Fila atualizada: ', lista_clientes)
                    break
            break
