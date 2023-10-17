# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'Seno: {sen: .2f} \t Cosseno: {cos: .2f} \t Tangente: {tg: .2f}.')