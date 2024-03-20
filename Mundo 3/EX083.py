'''Crie um programa onde o usuário digite uma empressão qualquer
que use parênteses. Seu aplicatuvi deverá analisar se a 
expressão passada está com os parênteses abertos e fechados
na ordem correta.
'''


expr = str(input('Digite a expressão: '))
listagem = []
for item in expr:
    if item == '(':
        listagem.append('(')
    elif item == ')':
        if len(listagem) > 0:
            listagem.pop()
        else:
            listagem.append(')')

if len(listagem) == 0:
    print('A expressão é válida! ')
else:
    print('A expressão não é válida.')


