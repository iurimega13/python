"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

n = int(input('Digite o valor a ser sacado: R$ '))
nota50 = n // 50
n %= 50
nota20 = n // 20
n %= 20
nota10 = n // 10
n %= 10
nota1 = n // 1

print('Notas de 50: {}'.format(nota50))
print('Notas de 20: {}'.format(nota20))
print('Notas de 10: {}'.format(nota10))
print('Notas de 1: {}'.format(nota1))