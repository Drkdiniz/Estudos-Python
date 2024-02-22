'''Faça um programa que jogue par ou ímpar com o computador. O
jogo só será interrompido quando o jogador perder, mostrando o total
de vitórias consecultivas que ele conquistou no final do jogo.'''

from random import randint
print('=-=-' * 10)
print(' '* 7 + ' JOGO DE PAR OU ÍMPAR')
print('=-=-' * 10)
cont = 0

while True:
    num = int(input('Digite um valor: '))
    computador = randint(1, 2)
    resultado = num + computador
    print('=-=-'*10)
    mao = input('Par ou ímpar?(Digite P para par ou I para ímpar): ').upper()
    print('=-=-'*10)
    cont += 1
    if mao not in 'PI':
        print('Digite P, I para escolher entre par ou ímpar!\n\n\n')
        continue
    
    #Condição de derrota onde o resultado é par e o jogador escolhe ímpar
    if resultado %2 == 0 and mao in 'I':
        print('Deu par, você perdeu, tente novamente!\n\n\n')
    
    #Condição de derrota quando o resultado é ímpar e o jogador escolhe par.
    elif resultado %2 != 0 and mao in 'P':
        print(f'Deu ímpar, você perdeu, tente novamente!')
    
    #Se as condições de derrota não forem cumpridas a pessoal será cumprimentada.
    else:
        print(f'Parabéns, você ganhou, foram necessárias {cont} tentativas.\n\n\n')
        break
   
    
    
    



