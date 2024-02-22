'''Crie um programa que leia vários números inteiros pelo teclado.
O prgorama só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles. (Desconsiderando o flag)'''

num = int (input('Digite um número (Digite 999 para parar): '))
soma = 0
cont = 0
while True:
    if num == 999:
        break
    soma += num
    cont += 1
    num = int (input('Digite um número (Digite 999 para parar: )'))
print(f'No total foram mostrados {cont} números e a soma entre eles é {soma}.')
    