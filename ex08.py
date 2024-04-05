'''Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela se ele é primo ou não usando o for.'''
num = int(input("Digite o número: "))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print('O número', primo, "é primo!")
else:
    print(num, 'não é número não é primo.')
