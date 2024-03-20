'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.

'''

valor = 0
valores = list()
for num in (range (0, 5)):
    valores.append(int(input(f'Digite um valor para a posição {num}: ')))
print('-='*25)
print(f'Você digitou os seguintes valores: {valores}')
valor_max=max(valores)
valor_min=min(valores)
print('-='*25)
print(f'O maior valor digitado foi {valor_max} nas posições | ',end='')
for pos, valor in enumerate(valores):
    if valor==valor_max:
        print(f'{pos}',end=' | ')
print(f'\nO menor valor digitado foi {valor_min} nas posições | ',end='')
for pos, valor in enumerate(valores):
    if valor==valor_min:
        print(f'{pos}',end=' | ')

        



    
