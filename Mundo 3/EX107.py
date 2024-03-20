


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except (ValueError, TypeError):
            print('\033[91mErro: você não digitou um valor válido!\033[0m')
        except KeyboardInterrupt:
            print('\n\033[91mErro: operação interrompida pelo usuário.\033[0m')
            raise

def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except (ValueError, TypeError):
            print('\033[91mErro: você não digitou um valor válido!\033[0m')
        except KeyboardInterrupt:
            print('\n\033[91mErro: operação interrompida pelo usuário.\033[0m')
            raise

# Código principal

valor_inteiro = 0
valor_decimal = 0

try:
    valor_inteiro = leiaint("Digite um número inteiro: ")
    valor_decimal = leiafloat("Digite um número decimal: ")
    print(f'Você digitou os valores {valor_inteiro} e {valor_decimal}')

except KeyboardInterrupt:
    
    if valor_inteiro != 0 or valor_decimal != 0:
        print(f'Você digitou os valores {valor_inteiro} e {valor_decimal}')
    
    else:
        print('\n\033[91mPrograma encerrado pelo usuário sem informar valores.\033[0m')
        

    


    



    