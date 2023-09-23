'''criar um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações 
possíveis sobre ele'''
texto = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(texto)}')
print(f'Só tem espaços? {texto.isspace()}')
print(f'É numérico? {texto.isnumeric()}')
print(f'É alfabético? {texto.isalpha()}')
print(f'É alfanumérico? {texto.isalnum()}')
print(f'Está em maiúsculo? {texto.isupper()}')
print(f'Está em minúsculo? {texto.islower()}')
print(f'Está capitalizada? {texto.istitle()}')