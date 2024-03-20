'''Faça um programa que leia o nome e media de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da
estrutura na tela.
'''

dicionario = dict()

dicionario['nome'] = input('Nome do aluno(a): ').capitalize()
dicionario['media'] = float(input('Media do aluno: '))

if dicionario['media'] >= 7:
    dicionario['situação'] = 'Aprovado'
    
else:
    dicionario['situação'] = 'Reprovado'
    
print('-='*25)
print('Informações do aluno:')
for chave, valor in dicionario.items():
    print(f'{chave.capitalize()}: {valor}')
    
