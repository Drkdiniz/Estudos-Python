#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais 
# alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


from time import sleep

a1 = int(input('Digite o número do primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))
cont = 1
pa = a1
termo = 1
termo = int(input('Digite o termo que gostaria de verificar (digite 0 para encerrar): '))
print(f'{pa} ', end='')
while termo != 0:
    while cont < termo:
        pa = pa + razao
        cont += 1
        print(f' - {pa} ',end='')
    termo = int(input('\nDigite o termo que gostaria de verificar (digite 0 para encerrar): '))
print('\n Encerrando o programa....')
sleep(1)
print('Tenha um ótimo dia.')       


        
            
            
            

    