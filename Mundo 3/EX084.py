'''Crie um algoritmo q leia o nome e peso de várias pessoas, 
guardando em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas; 
B) Uma lista com a pessoas mais pesadas; 
C) Uma lista com as pessoas mais leves.
'''


lista = []
dados = []
dados_max = []
dados_min = []
peso_max = 0
peso_min = 999


while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar? [s / n]: ').upper()
    
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Você deve digitar S para SIM ou N para não!')

for item in lista:
    if item[1] > peso_max:
        peso_max = item[1]
        dados_max = [item[0]]
    elif item[1] == peso_max:
        dados_max.append(item[0])
        
for item in lista:
    if item[1] < peso_min:
        peso_min = item[1]
        dados_min = [item[0]]
    elif item[1] == peso_min:
        dados_min.append(item[0])

print('-='*25)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {peso_max}kg. Peso de {dados_max}.') 
print(f'O menor peso foi de {peso_min}kg. Peso de {dados_min}.')  

    

