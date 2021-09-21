"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


def area(largura, comprimento):
    return largura * comprimento

titulo('Área de um Terreno')
largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))

print('A área do terreno de {}m x {}m é {}m²'.format(largura, comprimento, area(largura, comprimento)))