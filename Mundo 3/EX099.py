'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o 
maior.
'''

from time import sleep

def maior(* num):
    num_max = 0
    print('-='*35)
    print('Analisando os valores passados...',flush=True )
    sleep(2)
    print(f'Foram informados no tatal {len(num)} valores.',flush=True)
    sleep(2)
    print('Os valores informados foram: ',end='',flush=True)
    sleep(0.5)
    for i in num:
        print(f'{i}',end=' ',flush=True)
        sleep(0.5)
        if i > num_max:
            num_max = i
    print(f'\nO maior valor informado foi {num_max}.')
    sleep(1)
    
maior(3, 4, 5, 10, 2, 11, 12, 5, 20, 15, 31, 12, 9)
maior(4, 5, 6, 7, 3, 4, 10, 11, 2, 3)
maior(0)
maior(6)
maior()
print('-='*35)
        
    
        
        
            
    
    
