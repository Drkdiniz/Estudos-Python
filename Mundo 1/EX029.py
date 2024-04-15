#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.'''

#Forma 1 - Condição Composta
velocidade = int(input('Informe a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Sua velocidade é de {velocidade}KM/H.')
    print(f'Você foi multado em R${multa:,.2f} pelo excesso de velocidade!')
else:
    print(f'Você está a {velocidade}KM/H, boa viagem!')

 