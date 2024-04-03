'''Jogo de advinhação com 100 numeros, 7 tentetivas, ofecerer dica, oferecer se deseja sair'''
import random
numero = random.randint(1, 100)
print('='*20)
print('Advinhe um número entre 1 e 100')
tentativa = 0
while tentativa <= 7:
    adv = int(input('Advinhe o número: '))
    if numero == adv:
        print('Você Venceu!!!!!!!!!!')     
        break   
    else:
        tentativa += 1
        if adv > numero:
            print('Dica: você está muito quente, seu número é muito alto')
        else:
            print('Dica: Você está frio, jogue um número maior')
        escolha = input('Deseja continuar? (S/N)')
        escolha = escolha.lower()
        if escolha == 'n':
            break
print('Suas tentativas acabaram')
print('Fim do jogo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')