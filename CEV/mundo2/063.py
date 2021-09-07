"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
"""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' --> ')
        a, b = b, a + b
    print('FIM')
    
fib(int(input("Sequência de Fibonacci\n---------------------------------------------\nQuantos termos deseja mostrar? ")))