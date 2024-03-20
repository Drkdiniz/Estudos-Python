'''Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:
A- Quantidade de notas
B- A maior nota.
C- A média da turma
D- A situação (opcional)

'''
            
def notas(*num, situação=False):
    soma_nota = sum(num)
    total = len(num)
    maior_nota = max(num)
    menor_nota = min(num)
    
    media = soma_nota / total
    if situação:
        if media >= 7:
            situação = 'EXCELENTE'
        elif media > 5 and media <7:
            situação = 'AINDA TEM SALVAÇÃO'
        else:
            situação = 'Se FUDEU'
        return {'Total de notas':total, 'Maior nota':maior_nota, 'Menor nota':menor_nota, 
                'Média':media, 'Situação':situação}
    else:
        return {'Total':total, 'Maior nota':maior_nota, 'Menor nota':menor_nota, 
                'Média':media}
    
    
    
resp = notas(5.5, 9.5, 6, 6.5, situação=True)
print(resp)
    
   
            
    
        
    
            
            
            
    



