'''Crie um programa que crie uma matriz de dimensão 3 x3 e preencha
com valores lidos pelo teclado.
'''

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite o valor para [{linha} {coluna}]: '))
        matriz[linha].append(valor)
        
print('-='*25)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]',end=' ')
    print()
