#faça um programa que leia o ano de nascimento de um jovem e informe
# de acordo com sua idade
#-Se ele ainda vai se alistar ao serviço militar
#-Se é a hora de se alistar
#-Se já passou do tempo do alistamento

from datetime import datetime

ano = int(input('Digite seu ano de nascimento: '))
data = datetime.today().year
alistamento = data - ano
if alistamento < 18:
    print(f'Faltam {18-alistamento} anos para se alistar')

elif alistamento > 18:
    print(f'Se passaram {alistamento-18} anos do seu alistamento, regularize sua situação!')

else:
    print('É hora de se alistar!')
print('O Brasil precisa do seu comprometimento')