#Crie um programa que leia duas notas de um aluno e calcule sua média
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado 
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado

at1 = float(input('Digite a no da AT1: '))
at2 = float(input('Digite a nota da AT2: '))

média = (at1 + at2) / 2

if média < 5.0:
    print(f'Sua média foi de {média:.1f} e você foi reprovado!')

elif 5.0 >= média <= 6.9:
    print(f'Sua média foi de {média:.1f} e você ficou de recuperação!')

elif 7.0 >= média <= 9.9:
    print(f'Sua média foi de {média:.1f} e você foi aprovado!')

else:
    print('Você é foda!')