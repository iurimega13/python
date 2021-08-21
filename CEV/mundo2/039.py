"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

anoDeNascimento = int(input("Ano de nascimento -» "))

if date.today().year - anoDeNascimento >= 18:
    print("Você já passou do tempo de alistamento!")
elif date.today().year - anoDeNascimento >= 17:
    print('Esta é a hora de se alistar!')
else:
    print('Você tem que se alistar no ano de {}'.format(anoDeNascimento + 18))