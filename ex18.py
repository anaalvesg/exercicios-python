# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print(f'Seno: {sen: .2f} \t Cosseno: {cos: .2f} \t Tangente: {tg: .2f}.')