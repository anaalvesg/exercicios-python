# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))

# usando variável
desconto = preco - (preco * 0.05)
print(f'O preço do produto com desconto de 5% vai ficar: R$ {desconto}')

# direto no print
print(f'O preço do produto com desconto de 5% vai ficar: R$ {preco - (preco * 0.05)}')