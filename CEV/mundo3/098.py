"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep

def linha():
    print('-=-' * 30)
    
    
def contador(x, y, p):
    if x > y:
        y -= 1
        p = (p * -1)
    else:
        y += p
    for i in range(x, y, p):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    
linha()    
contador(1, 10, 1)
linha()    
contador(10, 0, 2)
linha()    

print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
linha()    