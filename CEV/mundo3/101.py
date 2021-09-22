"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import date
anoAtual = date.today().year

def titulo():
    print('-'*32)
    print('{:^32}'.format('VOTACAO'))
    print('-'*32)


def voto(idade):
    if idade >= 18:
        return 'OBRIGATÓRIO'
    elif idade >= 16:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


titulo()

anoDeNascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoDeNascimento

print('Com {} anos seu direito de voto é: {}'.format(idade, voto(idade)))