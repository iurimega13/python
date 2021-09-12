"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = []

for i in range(1,6):
    numeros.append(int(input('Digite o {}º número: '.format(i))))
    
maior = max(numeros)
menor = min(numeros)

print('Você digitou os valores {}'.format(numeros))
print('O maior valor digitado foi {} no indice {}'.format(maior, numeros.index(maior)))
print('O menor valor digitado foi {} no indice {}'.format(menor, numeros.index(menor)))