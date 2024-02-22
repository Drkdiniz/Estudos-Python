'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


cont=0
soma=0
media=0
maior=0
menor=999
num=int(input('Digite um número: '))
while True:
    if num > maior:
        maior=num
    if num < menor:
        menor=num
    soma+=num
    cont+=1
    media=(soma/cont)
    continuar=str(input('Deseja continuar? (Digite S para Sim ou N para encerrar): '))
    if continuar in'Nn':
        break
    num=int(input('Digite um número: '))
print(f'A média dos números inseridos é {media} ')
print(f'O menor número foi o {menor} e o maior número foi o {maior}')

   
    
    
