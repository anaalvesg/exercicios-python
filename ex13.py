# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$ '))

# usando variável
novo = salario + (salario * 0.15)
print(f'O salário com aumento de 15% ficará: R$ {novo}.')

# direto no print
print(f'O salário com aumento de 15% ficará: R$ {salario + (salario * 0.15)}.')