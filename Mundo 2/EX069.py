'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A- Quantas pessoas tem mais de 18 anos.
B- Quantos homens foram cadastrados.
C- Quantas mulheres tem menos de 20 anos.'''



print('=-=-' * 10)
print(' ' * 10 + 'CADASTRE UMA PESSOA')
print('=-=-' * 10)

maior_idade = 0
cont_woman = 0
cont_homem = 0

while True:
    while True: # Loop para obter a idade do usuário.
        idade = input('Idade: ')
        if idade.isdigit():
            idade = int(idade)
            if idade > 18:
                maior_idade += 1
            break # Sai do loop de entrada de idade.
        else:
            print("Por favor, digite uma idade válida.")

    #Loop para obter o sexo do usuário
    while True:
        sexo = input('Sexo: (H / M): ').upper()
        if sexo in 'HM':
            if sexo == 'H':
                cont_homem += 1
            break # Sai do loop de entrada de sexo.
        else:
            print("Por favor, digite 'H' para homem ou 'M' para mulher.")
    if sexo=='M' and idade < 20:
        cont_woman+=1
    
    # Loop para verificar se o usuário deseja continuar ou não.
    while True:
        continuação = input('Deseja continuar? (S / N): ').upper()
        if continuação in 'SN':
            break # Sai do loop de entrada da decisão.
        else:
            print("Por favor, digite 'S' para sim ou 'N' para não.")

    # Se o usuário decidir não continuar, exibe os resultados e encerra o programa.
    if continuação == 'N':
        print(f'Totalizamos {maior_idade} pessoas com mais de 18 anos.')
        print(f'Foram cadastrados {cont_homem} homens.')
        print(f'Totalizamos {cont_woman} mulheres com menos de 20 anos.')
        break 
        
        
        
    
        
            
        
        