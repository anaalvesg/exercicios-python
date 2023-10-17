# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. calcule e mostre o comprimento da hipotenusa.

from math import sqrt

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = co ** 2 + ca ** 2
print(f'\n O comprimento da hipotenusa é igual à {sqrt(hip): .2f}.')