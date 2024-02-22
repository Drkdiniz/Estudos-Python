#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


somador = 0
for num in range (1, 7):
    n1 = int(input(f'Digite o {num}º número: '))
    if n1 %2 == 0:
        somador = somador + n1
print(f'A soma dos números pares é {somador}.')
    
        