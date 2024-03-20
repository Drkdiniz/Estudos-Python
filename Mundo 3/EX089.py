''' Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
ontendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.
'''

boletim = []
cad = []
media = 0
while True:
    cad.append(input('Nome: ').upper())
    cad.append(float(input('Nota da AT1: ')))
    cad.append(float(input('Nota da AT2: ')))
    boletim.append(cad[:])
    cad.clear()
    cont = input('Deseja continuar?: ').upper()
    if cont == 'N':
        break
    elif cont != 'S':
        print('Você deve digitar S para SIM ou N para não.')



print('-='*18)
print('Nº',' '*7, 'NOME',' '*10, 'MÉDIA')
print('--'*18)

for indice, item in enumerate(boletim):
    media=(item[1] + item[2])/2
    print(f'{indice+1:<10} {item[0]:<15} {media}')
    
while True:
    nota = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if nota == 999:
        break
    else:
        print(f'AS notas do aluno {boletim[nota-1][0]} são {boletim[nota-1][1]} e {boletim[nota-1][2]}')
    

    


    