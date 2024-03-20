'''Dentro do pacote utilidadesCeV que criamos no desafio 1111, teremos 
um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
capaz de funcionar como a função input()mas com uma validação de dados para aceitar
apenas valores que sejam monetários.
'''


import moeda

num = moeda.leiadinheiro('Digite o preço R$: ')
moeda.resumo(num, 20, 20)
