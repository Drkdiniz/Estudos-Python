#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.'''

#Forma 1 - Condição Composta
velocidade = float(input('Qual a velocidade que você passou? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Dentro do limite! Boa viagem!')
else:
    print(f'Sua velocidade está acima de 80km/h! Você foi multado em: R${multa:.2f}')

 