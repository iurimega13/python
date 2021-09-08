"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

totalGasto = 0
totalMaisDe1000 = 0
nomeMaisBarato = ''
precoMaisBarato = 0
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    totalGasto += preco
    if preco > 1000:
        totalMaisDe1000 += 1
    if nomeMaisBarato == '':
        nomeMaisBarato = produto
        precoMaisBarato = preco
    elif preco < precoMaisBarato:
        nomeMaisBarato = produto
        precoMaisBarato = preco
    resposta = input('Deseja continuar? [S/N] ')
    if resposta in 'Nn':
        break
print('O total gasto foi de R${:.2f}'.format(totalGasto))
print('Temos {} produtos custando mais de R$1000'.format(totalMaisDe1000))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nomeMaisBarato, precoMaisBarato))