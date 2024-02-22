#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

soma = 0
contador= 0
n1 = int(input('Digite um número: '))
for num in range (1, n1+1):
    if n1 % num == 0:
        contador += 1
if contador == 2:
    print(f'O número {n1} é primo.')
else:
    (print(f'O número {n1} não é primo, ele possui {contador} divisores.'))