"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(1, 11):
    print('{}'.format(termo), end=' -> ')
    termo += razao
print('Acabou')