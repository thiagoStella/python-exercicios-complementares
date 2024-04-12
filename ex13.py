'''Ler as notas e mostrar na tela, são nove turmas, cada um com 24 alunos e cada aluno faz 5 testes'''
for i in range(1,10):
    print(f'Turma {i}')
    print('==========')
    for nome in range(1,25):
        nome = input('Digite o nome do aluno: ')
        media = 0
        for n in range(1,6):
            media += int(input(f'Digite a {n}ª nota: '))
        media = media / 5

for i in range(1,10):
    print(f'Turma {i}')
    print('==========')
    for j in range(1,25):
        print(f'O aluno {nome}, foi com a média {media}')
