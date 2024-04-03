'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e aquantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia mais R$0,15 por Km rodado'''
km = int(input("Qual a quilometragem rodada pelo carro: "))
dia = int(input("Quantos dias o carro ficou alugado: "))
km = km * 0.15
dia = dia * 60
print('O preço a pagar é de: R$', km + dia)
