"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os 
espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = input('Digite uma frase: ').replace(' ', '').upper()
fraseinvertida = frase[::-1]

print('O inverso de {} é {}\nTemos um palíndromo'.format(frase, fraseinvertida)) if frase == fraseinvertida else print('Não temos um palíndromo')