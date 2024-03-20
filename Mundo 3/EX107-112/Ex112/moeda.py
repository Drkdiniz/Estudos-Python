def dobro(preço=0, format=False):
    dobro = preço * 2
    return dobro if format is False else conv(dobro)

def metade(preço=0, format=False):
    metade = preço / 2
    return metade if format is False else conv(metade)

def aumentar(preço=0, taxa=0, format=False):
    aumentar = preço + (preço * taxa / 100)
    return aumentar if format is False else conv(aumentar)

def diminuir(preço=0, taxa=0, format=False):
    diminuir = preço - (preço * taxa / 100)
    return diminuir if format is False else conv(diminuir)
    
def conv(preço=0, moeda= 'R$'):
    return f'{moeda}{preço:>2.2f}'.replace('.',',')

def resumo(preço=0, taxa=10, taxa1=5,):
    print('-'*35)
    print('RESUMO DO VALOR'.center(30))
    print('-'*35)
    print(f'Valor analisado:\t {conv(preço)}')
    print(f'Dobro do preço:\t\t {dobro(preço, True)}')
    print(f'Metade do preço:\t {metade(preço, True)}')
    print(f'Com {taxa}% de aumento:\t {aumentar(preço, taxa, True)}')
    print(f'Com {taxa1}% de desconto:\t {diminuir(preço, taxa1, True)}')
    print('-'*35)
    
def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()  
        if entrada.isalpha() or entrada =='':
            print(f'ERRO: "{entrada}" é um preço inválido!')  
        else:
            return float(entrada)