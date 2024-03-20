'''Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto:
Negado, opcional ou obrigatório nas eleições.
'''


def voto(data_nasc):
    from datetime import date
    idade = (date.today().year - data_nasc)
    
    if idade < 16:
        print(f'Com {idade} anos você não pode votar.')
    
    elif idade >= 16 and idade <18 or idade > 70:
        print(f'Com {idade} anos seu voto é opcional.')
    
    else:
        print(f'Com {idade} anos seu voto é obrigatório.')
   
data_nasc = int(input('Informe a data de nascimento: '))
voto(data_nasc)
        

