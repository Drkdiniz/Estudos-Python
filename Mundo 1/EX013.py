# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float (input('Salário do funcionario: R$'))
aumento = salario + (salario*0.15)# Outra maneira seria salario + (salario * 15 / 100)
print(f'O seu salário com aumento de 15% é de R${aumento:.2f}')

