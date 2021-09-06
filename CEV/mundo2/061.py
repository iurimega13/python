"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

x = termo
i = 1
while i <= 10:
    print(x, end=' --> ')
    x += razao
    i += 1
print('FIM')