'''Faça um programa que tenha uma lista chamada números e duas funções 
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 
números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
números =list()

def sorteia(num):
    for _ in range(num):
        números.append(randint(0, 20))
    print(f'Os números sorteados foram {números}')
    
def somaPar():
    soma = 0
    for v in números:
        if v %2 == 0:
            soma += v
    print(f'A soma dos valores pares é igual a {soma}.')


sorteia(5)
somaPar()
