def dobro(n=0):
    dobro = n * 2
    return dobro

def metade(n=0):
    metade = n / 2
    return metade

def aumentar(n=0, taxa=0):
    aumentar = n + (n * taxa / 100)
    return aumentar

def diminuir(n=0, taxa=0):
    diminuir = n - (n * taxa / 100)
    return diminuir
    
def conv(n=0, moeda= 'R$'):
    return f'{moeda}{n:>2.2f}'.replace('.',',')