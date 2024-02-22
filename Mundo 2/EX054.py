#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e 
# quantas já são maiores. Considere a maior idade como 21 anos.

from datetime import date
cont_maior=0
cont_menor=0
data = date.today().year

for ano_nascimento in range (1, 8):
    ano_nascimento=int(input('Digite o ano de nascimento: '))
    if data-ano_nascimento>=18:
        cont_maior+=1
    else:
        cont_menor+=1
print(f'Ao todo {cont_maior} são maiores de idade e {cont_menor} são menores.')
        

    