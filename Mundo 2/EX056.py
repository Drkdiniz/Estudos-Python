#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, 
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somador_idade = 0
mais_velho = 0
homem_velho = ''
mais_nova = 999999
mulher_nova = ''
novinhas = 0

for c in range(1, 5):
    print(f'----{c}ª Pessoa----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo M/F: ').upper()
    somador_idade += idade
    media_idade = somador_idade / 4

#Estrutura condicional para comparar as idades dos homens
    if c==1 and sexo=='M':
        mais_velho=idade
        homem_velho=nome
    if idade > mais_velho and sexo=='M':
        mais_velho=idade
        homem_velho=nome
        
#Estrutura condicional para comparar a idade das mulheres
    if c == 1 and sexo == 'F':
        mais_nova = idade
        mulher_nova = nome
    if idade < mais_nova and sexo == 'F':
        mais_nova = idade
        mulher_nova = nome
        
        
#Estrutura para contar quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        novinhas += 1        

print(f'A média de idade das pessoas do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho é o {homem_velho} e tem {mais_velho} anos.')
print(f' A mulher mais nova é a {mulher_nova} e tem {mais_nova} anos.')
print(f' Ao todo tem {novinhas} mulheres com menos de 20 anos.')    
