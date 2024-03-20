'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga  mostrar os valores como um valor monetário formatado.


'''

import moeda

num = float(input('Digite um valor R$: '))
print(f'O dobro de R${moeda.conv(num)} é R${moeda.conv(moeda.dobro(num))}')
print(f'A metade de R${moeda.conv(num)} é R${moeda.conv(moeda.metade(num))}')
print(f'{moeda.conv(num)} com 10% de aumento é R${moeda.conv(moeda.aumentar(num, 10))}')
print(f'{moeda.conv(num)} com 15% de desconto é R${moeda.conv(moeda.diminuir(num, 15))}')
