'''Crie um programa que geerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
'''

jogador = {}
gol = []
gol_partida = total_gol = 0


jogador['nome'] = input('Nome do jogador: ').capitalize()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for g in range(jogador['partidas']):
    gol_partida = (int(input(f'Quantos gols na partida {g+1}?: ')))
    total_gol += gol_partida
    gol.append(gol_partida)
    jogador['gol'] = gol[:]
    jogador['total'] = total_gol
    

print('-='*25)
print(jogador)
print('-='*25)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
    
print('-='*25)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

print('-='*25)

for i, v in enumerate(jogador['gol']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
    
print(f'Foi um total de {total_gol} gols.')
    
