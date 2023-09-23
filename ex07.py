# desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))

# usando variável
media = (nota1 + nota2) / 2
print(f'Sua média é {media}')

# direto no print
print(f'Sua média é {(nota1 + nota2) / 2}')