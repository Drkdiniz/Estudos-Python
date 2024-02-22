#Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na tela a sua porção Inteira.

#Forma 1
import math
num = float(input('Insira um número: '))
inteiro = math.trunc(num)
print(f'O número {num} tem a parte Inteira: {inteiro} ')

#Forma 2
import math
num = float(input('Insira um número: '))
print(f'O número {num} tem a parte Inteira: {math.trunc(num)}')

