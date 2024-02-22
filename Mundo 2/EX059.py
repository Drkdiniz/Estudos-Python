'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''



n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

while True:
    print('MENU: ')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR NÚMERO')
    print('[4] ESCOLHER NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    
    while True:
        opção = (input('Escolha uma opção: '))
        
        if opção in ['1', '2', '3', '4', '5']:
            break
        
        else:
            print('Opção inválida, escolha um número entre 1 e 5.')
    
    if opção == '1':
        soma = n1 + n2
        print(f'{n1}+{n2}={soma}')
        break
    
    elif opção == '2':
        multiplicação = n1 * n2
        print(f'{n1}X{n2}={multiplicação}')
        break
    
    elif opção=='3':
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}.')
        
        elif n2 < n1:
            print(f'O número {n2} é maior que {n1}.')
        
        else:
            print(f'Os números são iguais.')
        break
    
    elif opção=='4':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    
    elif opção == '5':
        print('Obrigado por usar o programa.')
        break
        