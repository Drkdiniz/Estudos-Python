'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os 
alores pares e os valores ímpares digitados respectivamente
Ao final, mostre o conteúdo das três listas geradas.
'''

lista_geral = []
lista_impar = []
lista_par = []

while True:
    lista_geral.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar [S / N]?:  ').upper()
    
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Você deve digitar S para Sim ou N para não.')

for num in lista_geral:
    
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
        
print('-='*25)        
print(f'A lista completa é: {lista_geral}')
print(f'A lista dos números pares é: {lista_par}')
print(f'A lista dos números ímpares é: {lista_impar}')