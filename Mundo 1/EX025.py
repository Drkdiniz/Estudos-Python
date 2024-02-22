#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Forma 1
nome = str(input('Informe seu nome completo: ')).lower().strip()
condicao = 'silva' in nome
print(f'Seu nome tem Silva? {condicao}')

