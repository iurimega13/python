"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:                                                                                                                     ~~~~~~~~~~~~
 ola mundo!
~~~~~~~~~~~~                                                                        
"""
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    
txt = str(input('Digite algo: '))
escreva(txt)