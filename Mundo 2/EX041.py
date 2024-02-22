#A confederação nacional de natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo
#com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from datetime import datetime

nome = input('Qual o seu nome?: ')
data_nascimento = int(input('Digite seu ano de nascimento?: '))
data = datetime.today().year
categoria = data - data_nascimento

print(f'Olá {nome} Você tem {categoria} anos!')

if categoria <= 9:
    print(f'Você está qualificado para a categoria MIRIM.')

elif categoria <= 14:
    print(f'Você está qualificado para a categoria INFANTIL.')

elif categoria <= 19:
    print(f'Você está qualificado para a categoria JUNIOR.')

elif categoria <= 20:
    print(f'Você está qualificado para a categoria SENIOR.')

else:
    print(f'Você está qualificado para a categoria MASTER.')