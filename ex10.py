# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = carteira / 4.99

print('Você pode comprar US$ {:.2f}!' .format(dolar))
