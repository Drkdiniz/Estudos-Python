'''Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com
tamanho adaptável
'''

def escreva(msg):
    tam = len(msg) +4
    print('~'* tam)
    print(f'{msg.center(tam)}')
    print('~'* tam)
    
escreva('Derek')
escreva('Teste de função')
escreva('Uau')