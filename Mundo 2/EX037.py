#Escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão:
#1- Para binário
#2- Para octal
#3- Para hexadecimal

num = int(input('Digite o valor desejado: '))

print('Selecione a opção desejada')
print('1. Converter para binário')
print('2. Converter para octal')
print('3. Converter para hexadecimal')

n1 = int(input('Selecione a opção desejada: '))

if n1 == 1:
    print(f'O valor em binário é {bin(num)[2:]}')
elif n1 == 2:
    print(f'O valor em octal é {oct(num)[2:]}')
elif n1 == 3:
    print(f'O valor em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!')