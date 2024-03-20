def dobro(n=0, format=False):
    dobro = n * 2
    return dobro if format is False else conv(dobro)

def metade(n=0, format=False):
    metade = n / 2
    return metade if format is False else conv(metade)

def aumentar(n=0, taxa=0, format=False):
    aumentar = n + (n * taxa / 100)
    return aumentar if format is False else conv(aumentar)

def diminuir(n=0, taxa=0, format=False):
    diminuir = n - (n * taxa / 100)
    return diminuir if format is False else conv(diminuir)
    
def conv(n=0, moeda= 'R$'):
    return f'{moeda}{n:>2.2f}'.replace('.',',')