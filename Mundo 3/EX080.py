''' Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela
'''

indice=''
listagem= []

for _ in range(5):
    valor= int(input('Digite um valor: '))
    
    for indice, num in enumerate(listagem):
        
        if valor <= num:
            listagem.insert(indice, valor)
            print(f'O valor foi adicionado a posição {indice+1}')
            break
    
    else:
       listagem.append(valor)
       print('Valor adicionado ao fim da lista')
        
print(listagem)
        


    
    
   
        


    


