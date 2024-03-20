'''Aprimore o desafio anterior, mostrando no final:
A- A soma de todos os valores pares digitados;
B- A soma dos valores da terceira coluna;
C- O maior valor da segunda linha.
'''

matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite o valor para [{linha} {coluna}]: '))
        matriz[linha].append(valor)
        
        if valor % 2 == 0:
            soma_pares += valor
        if coluna == 2:
            soma_terceira_coluna += valor
        if linha == 1:
            if valor > maior_valor:
                maior_valor = valor
            
print('-='*25)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]',end=' ')
    print()
 
print('-='*25)   
   
print(f'A soma de todos os números pares é {soma_pares}.')
print(f'A soma de todos os números pares é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha foi {maior_valor}.')
        