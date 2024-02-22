#Refaça o desafio 35 dos triângulos acrescentando o recurso de 
#mostrar que tipo de triângulo será formado:
#-Equilátero
#-Isóceles
#-Escaleno


n1 = int(input('Insira o valor do primeiro vértice: '))
n2 = int(input('Insira o valor do segundo vértice: '))
n3 = int(input('Insira o valor do terceiro vértice: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    
    if n1 == n2 == n3:
        print('O triângulo é Equilátero!')
    
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('O triângulo é Isósceles')
    
    else:
        print('O triângulo é Escaleno')

else: 
    print('Esses vértices não formam um triângulo!')