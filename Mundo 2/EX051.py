#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão dessa PA: '))
an = n1 + (9 * razão)
for pa in range (n1, an+1, razão):
    print(f'{pa}',end='-')