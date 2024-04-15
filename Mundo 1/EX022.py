#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Qual o seu nome: ')
print(nome.upper())
print(nome.lower())
letras = nome.split()
print(f'Seu nome tem o total de: {len(''.join(letras))} letras')
print(f'O seu primeiro nome tem {len(letras[0])} letras')


