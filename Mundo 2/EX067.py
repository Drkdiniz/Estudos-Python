'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''

while True:
    num = int (input('Digite um número para calcular a tabuada: '))
    if num <= 0:#Coloquei o zero como condição de parada pois ele é um fator determinante na multiplicação.
        print('O número digitado precisa ser natural e maior que 0.')
        break
    cont = 0# Importante colocar o contador fora do loop interno para que ele seja resetado e volte a zero, caso contrário ele manterá o último resultado e a segunda tabuada consultada será afetada.
    resultado = 0
    while cont < 10:
        cont += 1
        resultado = num * cont
        print(f'{num} X {cont} = {resultado}')
    
    
        

    
    
        
    
    