#Faça um programa que leia o peso de cinco pessoas. No final, 
# mostre qual foi o maior e o menor peso lidos.

contador = 0
somador = 0
peso = 0
lista = []

for peso in range (1, 6):
    peso = float(input(f'Digite o peso da {peso}ª pessoa: '))
    lista.append(peso)
    lista.sort()

print(f'O menor peso lido é {lista[0]}KG')
print(f'O maior peso lido é {lista[-1]}KG')
    
    