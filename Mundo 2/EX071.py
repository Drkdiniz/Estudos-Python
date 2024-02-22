'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues'''

print('=-='*10)
print(' '*10 + 'BANCO DEREK')
print('=-='*10)
saque=int(input('Digite o valor para sacar: '))
valor = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
#Enquanto o valor do saque for maior que zero o programa rodará o lopp
while saque > 0:
    #Enquanto o valor do saque for maior ou igual a 50 ele subtrairá esse valor e o
    #contador indicará o número de cédulas , e o mesmo vale para os demais.
    if saque >= 50:
        saque -= 50
        cont_50 += 1
    elif saque >= 20:
        saque -= 20
        cont_20 += 1
    elif saque >= 10:
        saque -= 10
        cont_10 += 1
    elif saque >= 1:
        saque -= 1
        cont_1 += 1

print(F'Total de {cont_50} cédulas de R$ 50.')
print(f'Total de {cont_20} cédulas de R$ 20.')
print(f'Total de {cont_10} cédulas de R$ 10.')
print(f'Total de {cont_1} cédulas de R$ 1.')
print('=-='*10)
print('Volte sempre e tenha um ótimo dia!')

 #Corrigi o while colocando maior que zero, o programa estava travando pois 
 # o loop estava programado para continuar enquanto o saque fosse >=0 e 
 # como o saque tinha condição de parada quando chegasse a 1  loop se tornou infinito.
        
 