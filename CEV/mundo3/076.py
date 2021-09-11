"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('lapis', 1.75,
            'caneta', 2.50,
            'caderno', 15.90,
            'estojo', 25.00,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'borracha', 3.45)
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R${:>7.2f}'.format(listagem[pos]))

print('-' * 40)