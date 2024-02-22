#Crie um programa que faça o computador jogar Jokenpô com você.

import random
print('''Escolha uma opção:
[ ] Pedra
[ ] Papel
[ ] Tesoura
 ''' )

jogador = str(input('Digite sua escolha: '))
lista = ['Pedra','Papel','Tesoura']
computador = random.choice(lista)

print(f'Você escolheu {jogador} e o computador escolheu {computador}')

if jogador=='Pedra' and computador=='Pedra':
    print('Empatou!')

elif jogador=='Pedra' and computador=='Papel':
    print('Computador ganhou!')

elif jogador=='Pedra' and computador=='Tesoura':
    print('Jogador ganhou!')

elif jogador=='Papel' and computador=='Pedra':
    print('Jogador ganhou!')

elif jogador=='Papel' and computador=='Papel':
    print('Empatou')

elif jogador=='Papel' and computador=='Tesoura':
    print('Computador ganhou!')

elif jogador=='Tesoura' and computador=='Pedra':
    print('Computador ganhou!')

elif jogador=='Tesoura' and computador=='Papel':
    print('Jogador ganhou!')

elif jogador=='Tesoura' and computador=='Tesoura':
    print('Empatou')

else:
    print('Erro')