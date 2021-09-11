"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = ()

for i in range(5):
    numeros += (randint(1, 10),)

print('Os números sorteados foram: {}'.format(numeros))
print('O maior número sorteado foi: {}'.format(max(numeros)))
print('O menor número sorteado foi: {}'.format(min(numeros)))