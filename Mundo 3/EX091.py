'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking =()

print('-='* 25)
print(' '* 15 + 'VALORES SORTEADOS')
print('-='* 25)
sleep(2)

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*25)
print(' '*15 +'RANKING DOS JOGADORES')
print('-='*25)
sleep(1)

for indice, valor in enumerate(ranking):
    print(f'{indice + 1}º lugar: {valor[0]} tirou {valor[1]} nos dados.')
    sleep(1)
    