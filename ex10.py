'''. Escreva um algoritmo para verificar se uma palavra é um palíndromo usando o while'''
palavra = input('Digite uma palavra: ')
i = 0
j = len(palavra) - 1
palindromo = True

while i < j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1

if palindromo:
    print('A palavra é um palindromo')
else:
    print('A palavra não é um palindromo')

