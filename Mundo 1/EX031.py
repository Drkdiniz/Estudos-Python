#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

#Forma 1
distancia = float(input('Qual a distância da viagem em km? '))   
if distancia <= 200:
   preço = distancia * 0.50
   print(f'Sua viagem é {distancia}km, logo sua passagem custa R${preço:.2f}')
else:
   preço = distancia * 0.45
   print(f'Sua viagem é {distancia}km, logo sua passagem custa R${preço:.2f}')