"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint

def sorteia():
    temp = []
    for i in range(5):
        temp.append(randint(1, 10))
    return temp


def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    return soma

numeros = sorteia()

somaPar = somaPar(numeros)

print('Soteando 5 valores...')
print('OS valores sorteados foram: ', end='')
for i in numeros:
    print('{}'.format(i), end=' ')
print()
print('Somando valores pares...')
print('A soma dos valores pares sorteados é: {}'.format(somaPar))
    
