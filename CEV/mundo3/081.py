"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)

    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Tente novamente. Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break

print('Foram digitados {} elementos!'.format(len(valores)))
print('Os valores em ordem decrescente são: {}'.format(sorted(valores, reverse=True)))
print('O valor 5 faz parte da lista' if 5 in valores else 'O valor 5 não faz parte da lista')