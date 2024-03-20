'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.

'''

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
          'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 
          'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
          'dezenove', 'vinte')

while True:
    n1 = int(input('Digite o número que gostaria de ver por extenso: '))
    if n1 <= 20:
        print(f'Você digitou o número {numero[n1]}')
        continuar=input('Você gostaria de continuar? [S / N]: ').upper()
        
        while continuar not in 'NS':
            print('Erro, por favor digite S para Sim ou N para não.')
            continuar=input('Você gostaria de continuar? [S / N]: ')
        
        if continuar in 'N':
            break
    else:
        print('Erro, você deve escolher um número entre 0 e 20!')

    

   