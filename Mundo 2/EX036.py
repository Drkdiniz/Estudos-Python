#Escreva um programa para aprovar o empréstimo bancário para a 
#compra de uma casa. O programa vai perguntar o valor da casa
# o salário do comprador e em quantos anos ele vai pagar.

valor_imovel = float(input('Qual o valor do imóvel?: '))
salario = float(input('Qual o valor do seu salário?: '))
tempo = float(input('Em quanto tempo deseja pagar (anos)?: '))

prestação=valor_imovel/(tempo*12)

if prestação>(salario*0.3):
    print('''O valor da prestação excede 30% do seu salário, 
          portanto o empréstimo foi negado ''')
else:
    print('''Você cumpre os requisitos mas não fui com a sua cara,
          empréstimo negado!''')