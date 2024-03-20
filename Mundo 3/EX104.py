'''Crie um programa que tenha a função leaiint(), que vai funcionar
de forma semelhante à função input() do python, só que fazendo
a validação para aceitar apenas um valor numérico.
'''


def leiaint(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            valor = int(valor)
            return valor
            break
        else:
            print('\033[91mErro: você não digitou um valor válido!\033[0m')
        
#Código principal
num = leiaint("Digite um número inteiro: ")
print(f'Você digitou o valor {num}')
