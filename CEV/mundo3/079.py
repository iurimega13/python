"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

vaores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in vaores:
        vaores.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 40)
print('Você digitou os valores {}'.format(sorted(vaores)))