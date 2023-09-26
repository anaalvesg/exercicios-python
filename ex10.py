# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 4.99

x = carteira / dolar
print('Você pode comprar {:.2f} dólares!' .format(x))
