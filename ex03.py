'''Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta a ser usada, cada litro de tinta pinta 2m²'''
alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura: "))
area = alt * larg
print("Para pintar a parede serão necessarios {:.2f} litros de tinta".format(area / 2))