'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

import random
import time
print('-'*50)
print('JOGO DA MEGA SENA'.center(50))
print('-'*50)
lista = list(range(1, 61))
quantidade = int(input('Quantos jogos você quer que eu sorteie?: ') )

print(f'-=-=-= SORTEANDO {quantidade} JOGOS-=-=-=')

for _ in range (0, quantidade):
    numeros_aleatorios = random.sample(lista, 6)
    print(f'{sorted(numeros_aleatorios)}')
    time.sleep(1)
    
print('BOA SORTE!')


