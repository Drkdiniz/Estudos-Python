#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número 
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.


from random import randint

cont = 0
computador = randint(0, 10)
jogador = ''

print(f'COMPUTADOR: Você consegue adivinhar em que número estou pensando?!')

while computador != jogador:
    jogador = int(input('Em qual número estou pensando?: '))
    cont += 1
    
    if computador == jogador:
        print(f'Parabéns, você acertou, eu escolhi o número {jogador}.')
    
    else:
        if jogador < computador:
            print('ERROU!!!')
            print(f'DICA: Você precisa tentar um número maior.')
        
        elif jogador > computador:
            print('ERROU!!!')
            print(f'DICA: Você precisa tentar um número menor')

print(f'Você acertou com {cont} tentativas.')
    
    
    

