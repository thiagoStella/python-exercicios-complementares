'''Faça um código em Python que leia o nome do aluno, leia uma quantidade indefinida de notas digitadas pelo 
professor e,ao final, faça o cálculo da média e imprima o nome do aluno e sua média correspondente.'''
cont = 0
soma = 0
nome = input('Digite o nome do aluno: ')
while True:
    nota = float(input('Digite a nota a ser somada: '))
    print('===ZERO para calcular a média===')
    if nota == 0:
        break
    else:
        cont += 1
    soma += nota
media = soma / cont
print('A média do aluno', nome, 'foi de', media)
