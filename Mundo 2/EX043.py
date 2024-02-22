#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
#seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do peso.
#-Entre 18.5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidade
#-Acima de 40: Obesidade mórbida

peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do peso ! ')

elif imc <= 25:
    print(f'Seu IMC é {imc:.1f} e você está no peso ideal ! ')

elif imc <= 30:
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso ! ')

elif imc <= 40:
    print(f'Seu IMC é {imc:.1f} e você está obeso ! ')

else:
    print(f'Seu IMC é {imc:.1f} e você está com obesidade mórbida! ')