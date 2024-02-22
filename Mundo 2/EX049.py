#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário 
# escolher, só que agora utilizando um laço for.

n1=int(input('Digite o número da tabuada que gostaria de exibir: '))#Número que será utilizado para exibir a tabuada.
soma=0
contador=0
for tabuada in range (11):#Criei a variável tabuada com uma lista que vai de 0-10 para que essa repetição sirva de base para o cálculo da tabuada.
        resultado=tabuada*n1#Criei uma variável que vai multiplicar os valores do for e da entrada input.
        print(f'{n1} X {tabuada} = {resultado}')#print do resultado da multiplicação.