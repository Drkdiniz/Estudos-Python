'''Aprimore o desafio 93 para que ele funcione com vários jogadores
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''

jogadores = []
gol_partida = []
total_gol = 0

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    
    for g in range(jogador['partidas']):
        gol_na_partida = (int(input(f'Quantos gols na partida {g+1}?: ')))
        total_gol += gol_na_partida
        gol_partida.append(gol_na_partida)
    jogador['gols_por_partida'] = gol_partida[:]
    jogador['total_gols'] = total_gol
    jogadores.append(jogador.copy())
    gol_partida.clear()
    total_gol = 0
    continuar = input('Deseja continuar? [S / N]: ').upper()
    
    while continuar not in 'SN':
        print('Você deve digitar S para continuar ou N para encerrar o cadastramento.')
        continuar = input('Deseja continuar? [S / N]: ').upper()
            
    if continuar == 'N':
        break

print('-='*25)

for indice, jogador in enumerate(jogadores):
    nome = jogador['nome']
    gols_por_partida = jogador['gols_por_partida']
    total_gols = jogador['total_gols']
    print(f'{indice+1} - Jogador: {nome}, Gols por Partida: {gols_por_partida}, Total de Gols: {total_gols}') 

while True:      
    dados_jogador = int(input('Mostrar dados de qual jogador?: '))
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[dados_jogador-1]['nome']} ')
    for indice, v in enumerate(jogadores[dados_jogador-1]['gols_por_partida']):
        print(f'No jogo {indice+1} fez {v} gols.')
    continuar = input('Deseja continuar? [S / N]: ').upper()
    
    while continuar not in 'SN':
        print('Você deve digitar S para continuar ou N para encerrar o cadastramento.')
        continuar = input('Deseja continuar? [S / N]: ').upper()
            
    if continuar == 'N':
        print('===ENCERRANDO===')
        break