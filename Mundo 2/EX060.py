#Faça um programa que leia um número qualquer e mostre o seu fatorial.

n1 = int(input('Digite um número para saber o fatorial: '))
somador = n1
fatorial = 1

print(f'Calculando o fatorial de {n1}!: ',end='')

while somador > 0:
    fatorial = fatorial * somador
    print(f'{somador}',end='')
    print(f' X ' if somador >1 else ' = ',end='')
    somador -= 1
    
print(f'{fatorial}',end='')

fatorial = 1
n1 = int(input('Digite um número: '))
for c in range (1, n1+1):
    fatorial = fatorial * c
print(fatorial)
    
    
    



    

    
    
    