'''Crie um algoritmo que pede ao usuário para que digite um número inicial e um número final. 
Em seguida, ele mostrará todos os números pares neste intervalo usando FOR.'''
inicial = int(input('Digite o número inicial: '))
final = int(input('Digite o número final: '))
for num in range(inicial, final):
    if num % 2 == 0:
        print(num)


