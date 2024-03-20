'''Crie um programa que leia nome, ano de nascimento e CTPS e cadastre-os 
(com idade) em um dicionário, se por acaso a CTPS for diferente de 
zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar.
'''

from datetime import datetime

trabalhador = {}

trabalhador['nome'] = input('Nome: ').capitalize()
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
trabalhador['idade'] = ano_atual - ano_nascimento
trabalhador['ctps'] = int(input('Carteira de Trabalho (digite 0 caso não tenha): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    ano_aposentadoria = trabalhador['contratação'] + 35
    aposentadoria = (ano_aposentadoria - ano_nascimento)
    if aposentadoria <= 65:
        trabalhador['aposentadoria'] = aposentadoria
    else: 
        trabalhador['aposentadoria'] = 65
   
print('-='* 25)
for k, v in trabalhador.items():
    print(f'{k.capitalize()}: {v}')
       
   
   


print(trabalhador)
