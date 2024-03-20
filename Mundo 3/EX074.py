'''Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.

'''

from random import randint
num = tuple(randint(0, 100) for num in range (5))

print(f'Os 5 números gerados são: {num}')
print(f'O menor valor na tupla é o {min(num)}')
print(f'O maior valor na tupla é o {max(num)}')


