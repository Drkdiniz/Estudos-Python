'''Crie um programa onde o usuário possa digitar Sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os
valores PARES e ÍMPARES. No final mostre os valores pares
e ímpares em ordem CRESCENTE.
'''

lista = [[],[]]

for num in range(7):
    valor = int(input(f'Digite o {num+1}º valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print('-='*25)        
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')