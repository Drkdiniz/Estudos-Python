'''Faça um programa que tenha uam função chamada contador(), que
receba três parâmetros: início, fim e passo e realize uma contagem.
'''

from time import sleep

def contador(a, b, c):
    print('-='*25)
    print(f'Contagem de {a} até {b} de {c} em {c}:') 
    #Caso o passo seja igual a zero o programa vai transformar em 1
    if c == 0:
        c = 1
        
    #Estrutura condicional para situações em que o primeiro termo
    #é maior que o último
    if a > b:
        c = -abs(c)
        for num in range(a, b-1, c):
            print(f'{num}',end='...', flush=True)
            sleep(0.5)
        
   #Estrutura condicional para situações em que o primeiro termo
    #é menor que o termo final
    if a < b:
        c = abs(c)
        for num in range(a, b+1, c):
            print(f'{num}',end='...', flush=True)
            sleep(0.5)
        
    print('FIM!')
        
contador(1, 10, 1)
contador(10, 0, 2)
 
print('-='*25)   
print('Agora é a hora de personalizar a contagem!')

a1 = int(input('Início: '))
an = int(input('FIM: '))
passo = (int(input('Passo:')))

contador(a1, an, passo)

print('-='*25)           
print('FIM!')

   
        
        
     
            
        
                
    
            
    
  
            
  

            
        
   
        
   

     
        
            
        


    
        
    




