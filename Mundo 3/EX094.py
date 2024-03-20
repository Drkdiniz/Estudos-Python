'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A-Quantas pessoas foram cadastradas
B-A média de idade do grupo
C-Uma lista com todas as mulheres
D-Uma lista com todas as pessoas com idade acima da média.
'''



cad = {}
lista = []
lista_velhos = []
soma_idade = media_idade = 0

while True:
    cad['nome'] = input('Nome: ').capitalize()
    sexo = input('Sexo [M / F]: ').upper()
    
    while sexo not in 'MF':
        print('Você deve digitar M para masculino e F para feminino.')
        sexo = input('Sexo [M / F]: ').upper()
        
    cad['sexo'] = sexo
    cad['idade'] = int(input('Idade: '))
    soma_idade += cad['idade']
    lista.append(cad.copy()) 
    cad.clear()  
    print('Valores adicionados com sucesso!')
    continuar = input('Deseja continuar? [S / N]: ').upper()
    
    while continuar not in 'SN':
        print('Você deve digitar S para continuar ou N para encerrar o cadastramento.')
        continuar = input('Deseja continuar? [S / N]: ').upper()
            
    if continuar == 'N':
        break

print('-='*25)
print(f'No total foram cadastradas {len(lista)} pessoas.')
media_idade = (soma_idade / len(lista))
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: ',end=' ') 
    
for i in lista:    
    if i['sexo'] == 'F':
        print(f'{i["nome"]}',end='; ')
print()
        
print('Lista das pessoas acima da média de idade: ')
for i in lista:
    if i['idade'] > media_idade:
        lista_velhos.append(i.copy())        
        
for pessoa in lista_velhos:
    print(f'Nome: {pessoa["nome"]}; Idade: {pessoa["idade"]}; Sexo: {pessoa["sexo"]}')
  
    
    
        
    

        


        




            





    
        
    




