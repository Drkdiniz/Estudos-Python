'''Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.

'''

import moeda

num = int(input('Digite um valor R$: '))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'R${num} com 10% de aumento é R${moeda.aumentar(num)}')
print(f'R$ {num} com 15% de desconto é R${moeda.diminuir(num)}')
