'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final. mostre:
A- Qual o total gasto
B- Quanto produtos custam mais de R$1000
C- Qual é o nome do produto mais barato.
'''

print('=-='*10)
print(' '*10 + 'CASAS BAHIA')
print('=-='*10)
total_gasto = 0
produto_caro = 0
preço_barato = 9999
produto_barato = ''


while True:
    # Loop para garantir que o nome do produto não esteja em branco
    while True:
        nome = input('Nome do produto: ').upper()
        if not nome.strip():
            print('O nome do produto não pode ficar em branco.')
        
        else:
            break
    
    #Loop para registrar os valores gastos
    while True:
        preço = float(input('Preço do produto R$: '))
        total_gasto += preço
        
        #Soma ao contador produto_caro todo produto que custar acima de 1000 reais.
        if preço > 1000:
            produto_caro += 1
        
        #Condicional para comparar o mostrar o produto mais barato
        if preço_barato > preço:
            preço_barato = preço
            produto_barato = nome
        break
        
    # Loop para verificar se o usuário deseja continuar adicionando produtos
    while True:
        continuar = input('Deseja continuar? (S / N): ').upper()
        
        if continuar not in 'SN':
            print('Digite S para sim e N para não.')
        
        if continuar in 'SN':
            break
    
    # Se o usuário não desejar continuar, exibe os resultados e encerra o programa.
    if continuar in 'N':
        print('=-='*6+ ' FIM DO PROGRAMA '+ '=-='*6)
        print(f'O total gasto foi de R$ {total_gasto:.2f}')
        print(f'Ao todo {produto_caro} custaram mais de 1000 reais.')
        print(f'O produto mais barato foi o {produto_barato}, custando {preço_barato:.2f}.')
        break