'''Crie um programa que tenha uma função fatorial() que receba dois
parâmetros:
1-Indique o número a calcular
2-O segundo parâmetro será chamado sohw que será um valor lógico opcional
indicando se será mostrado o calculo em tela.
'''

def fatorial(num, show=False):
    
    resultado = num
    cont = num - 1
    
    while cont >= 1:
        resultado *= cont
    
        if show:
            print(f'{num} x {cont}', end='; ')
        cont -= 1
    
    if show:
        print(f'= {resultado}')
    
    return resultado
    
print(fatorial(5, show=True))
    
    
   
   
   
