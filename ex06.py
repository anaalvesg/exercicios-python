# criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
num = int(input('Digite um número: '))

# usando variável
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)
print(f'O dobro do número é {dobro}, o triplo é {triplo}, e sua raiz quadrada é {raiz}')

# direto no print
print(f'O dobro do número é {num * 2}, o triplo é {num * 3}, e sua raiz quadrada é {sqrt(num)}')