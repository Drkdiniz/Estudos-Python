''' Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso mostre:
A-Quantos números foram digitados
B-A lista de valores, ordenada de forma decrescente
C- Se o valor 5 foi digitado e está ou não na lista.
'''


lista = []
num_5 = []

while True:
    num=int(input('Digite um número: '))
    lista.append(num)
    continuar=input('Deseja continuar [S / N]: ').upper()
    
    if continuar == 'N':
        break
    if continuar not in 'S':
        print('Você deve digitar S para SIM ou N para não.')
        
for indice, num in enumerate(lista):
    if num == 5:
        num_5.append(indice + 1)

print('=-' * 35)
print(f'Total de números digitados: {len(lista)} ')
print(f'Lista ordenada em ordem decrescente: {sorted(lista, reverse=True)}')

if len(num_5) > 0:
    print(f'O número 5 foi digitado nas posições: {num_5}')
else:
    print('O número 5 não foi digitado na lista.')
    
        
    