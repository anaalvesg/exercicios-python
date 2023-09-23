# fazer um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número inteiro: '))

# usando variável
ant = num - 1
suc = num + 1
print(f'O antecessor de {num} é {ant}, e seu sucessor é {suc}')

# direto no print
print(f'O antecessor de {num} é {num - 1}, e seu sucessor é {num + 1}')