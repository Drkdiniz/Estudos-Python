''' Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados em ordem crescente.
'''

listagem=[]

listagem.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso !')

while True:
    continuar=input('Deseja continuar [S / N]: ').upper()
    
    if continuar == 'S':
        valor=(int(input('Digite um valor: ')))
        
        if valor not in listagem:
            listagem.append(valor)
            print('Valor adicionado com sucesso !')
        else:
            print('Esse valor já existe e não foi adicionado.')
    
    elif continuar == 'N':
        break
    
    else:
        print('Você deve dgitar ''S'' para SIM ou ''N'' para NÂO.')
    
print(f'Você digitou os valores: {sorted(listagem)}')
        
    
    
