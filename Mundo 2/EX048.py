#Faça um programa que calcule a soma entre todos os números que são 
# múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
for num in range(1,501,2):
    if num % 3 == 0:
        print(num, end=' ')
        s+=num
print(f'A soma entre esses valores é de {s}')
