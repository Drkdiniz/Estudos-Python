#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando 
# os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o número do primeiro termo: '))
razão = int(input('Digite a razão dessa PA: '))
an = 10
pa = a1
cont = 1
while cont < an:
    print(f'{pa} -',end=' ')
    pa = pa + razão
    cont += 1
print(f'{pa}',end=' ')


    
    