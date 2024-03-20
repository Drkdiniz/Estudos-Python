'''Modifique as funções que foram criadas no desafio 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

'''

import moeda

num = float(input('Digite um valor R$: '))
print(f'O dobro de R${moeda.conv(num)} é R${moeda.dobro(num, True)}')
print(f'A metade de R${moeda.conv(num)} é R${moeda.metade(num, True)}')
print(f'{moeda.conv(num)} com 10% de aumento é R${moeda.aumentar(num, 10, True)}')
print(f'{moeda.conv(num)} com 15% de desconto é R${moeda.diminuir(num, 15, True)}')
