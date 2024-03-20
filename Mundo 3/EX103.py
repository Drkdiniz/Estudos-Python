'''Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: Nome e gols de um jogador. O programa
deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
'''


def ficha(nome='<desconhecido>', gol=0):
    
    return print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')
   
    

print('--'*25)
nome = input('Nome do jogador: ').capitalize()
gol = input('Número de gols: ')

if gol.isnumeric():
    gol = int(gol)

else:
    gol = 0
    
if nome.strip() =='':
    ficha(gol=gol)

else:
    ficha(gol=gol, nome=nome)
