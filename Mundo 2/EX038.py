#Escreva um programa que leia dois números inteiros e compare-os
#mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais.


num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))

if num_1 > num_2:
    print(f'O valor {num_1} é maior.')

elif num_2 > num_1:
    print(f'O valor {num_2} é maior.')

else:
    print('O valores são iguais')