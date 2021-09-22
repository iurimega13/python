"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def titulo():
    print('\n' + '-' * 50)
    print('{:^50}'.format('FATORIAL'))
    print('-' * 50)


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :print: Imprime o resultado do fatorial.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


titulo()

num = int(input('Digite um número para se calcular o fatorial: '))
show = input('Mostrar o processo de cálculo? [S/N] ').upper()
if show == 'S':
    show = True
else:
    show = False

fatorial(num, show)