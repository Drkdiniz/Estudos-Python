#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo not in ['F', 'M']:
    sexo = (input('Digite o sexo: ')).upper()
    if sexo not in ['F', 'M']:
        print('Você precisa digitar M ou F para escolher o sexo.')

print(sexo)