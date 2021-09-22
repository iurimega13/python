"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randint

def linha():
    print('-=-' * 30)


def maior(numeros):
    print('Analisando os valores passados...')
    print('Foram informados {} valores a serem analisados.'.format(len(numeros)))
    print('Os valores informados foram {}'.format(numeros))
    print('O maior valor informado foi {}'.format(max(numeros)))


for i in range(5):
    linha()
    numeros = ()
    for j in range(randint(1, 10)):
        numeros += (randint(1, 10),)
    maior(numeros)