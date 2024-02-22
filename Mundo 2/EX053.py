#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos: 
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


n1 = str(input('Digite uma frase: '))

lista = [n1]

for frase in lista:
    frase = frase.upper().replace(' ','').split()
    frase_invertida = frase[::-1]
print(f'{frase}{frase_invertida}') 

if frase == frase_invertida:
    print(f'A frase "{n1}" é um palíndromo.')

else:
    print(f'A frase "{n1}" não é um palíndromo.')
    

