''' Desafio 76
 Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.
'''

produto=''
preço=''

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro',
            34.90
            )

print('-'*45)
print(F'{'LISTA DE PREÇOS':^45}')
print('-'*45)

for item in range(0, len(listagem), 2):
    produto = listagem [item]
    preço = listagem [item + 1 ]
    print(f'{produto:.<38} {preço:<.2f}')

print('-'*45)
            

