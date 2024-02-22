#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
# aparece a letra "A", em que posição ela aparece a primeira vez e em 
# que posição ela aparece a última vez.


frase = str(input('Informe uma frase qualquer: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira posição da letra A é {frase.find('A')+1} e a última é {frase.rfind('A')+1}')