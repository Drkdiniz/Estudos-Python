#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe mais um número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior')
if n2 > n1 and n2 > n3:    
    print(f'O número {n2} é o maior')
if n3 > n1 and n3 > n2:    
    print(f'O número {n3} é o maior')
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor')
if n2 < n1 and n1 < n3:
    print(f'O número {n1} é o menor')
if n3 < n1 and n1 < n2:
    print(f'O número {n1} é o menor')