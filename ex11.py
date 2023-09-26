'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

a = larg * alt
tinta = a / 2

print(f'Sua parede de dimensão {larg}x{alt} tem uma área de {a}m². São necessários {tinta}L de tinta.')