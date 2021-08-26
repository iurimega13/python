"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input("Digite um número: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[32m{}\033[m'.format(i), end=' ')
        count += 1
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
print('\nO número {} foi divisível {} vezes'.format(num, count))
print('E por isso ele é PRIMO!' if count <= 2 else 'E por isso ele NÃO é PRIMO!')