from interface import*
from arquivo import*
from time import sleep

arq = 'sistemadecontrole.txt'

if not arquivo(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        LerArquivo(arq)
    
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa!
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    
    else:
        print('\n\033[91mErro: Digite uma opção válida!\033[0m')
    
    sleep(1)
