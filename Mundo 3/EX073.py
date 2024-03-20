'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A- Apenas os 5 primeiros colocados.
B- Os últimos 4 colocados da tabela.
C- Uma lista com os times em ordem alfabética.
D- Em que posição na tabela está o time da Chapecoense.

'''

brasileiro= ('Palmeiras', 'Flamengo', 'Inter', 'Grêmio', 'São Paulo',
       'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
       'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 
       'Vasco', 'América-MG', 'Sport', 'Vitória', 'Paraná')

    
print(f'Lista dos times do Brasileirão: {brasileiro}\n')
print(f'Os 5 primeiros times na tabela são: {brasileiro[0:5]}\n')
print(f'Os últimos 4 times na tabela são: {brasileiro[-4]}\n')
print(f'Organização dos times por ordem alfabética: {sorted(brasileiro)}\n')
print(f'O time chapecoense está na {brasileiro.index('Chapecoense')+1}ª posição na tabela.\n')