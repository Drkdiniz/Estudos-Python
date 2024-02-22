'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''


n = int(input('Digite o termo desejado: '))
a1 = 0
a2 = 1
a3 = 1
cont = 2
print(f'{a1} - {a2}',end='')
while cont < n:
    a3 = a1 + a2
    a1 = a2
    a2 = a3  
    cont += 1
    print(f' - {a3}',end='')  
    
       



    
    
