'''Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno
'''

def multiplica(a, b):
    s = a * b
    print(f'A área de um terreno de {a}X{b} é de {s}m2.')


a = (float(input('Largura (m): ')))
b = (float(input('Comprimento(m): ')))

multiplica(a, b)