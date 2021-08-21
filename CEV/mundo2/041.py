"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

from datetime import date

anoDeNascimento = int(input('Digite o ano de nascimento: '))

if (anoDeNascimento >= date.today().year - 9):
    print('MIRIM')
elif (anoDeNascimento >=date.today().year - 14):
    print('INFANTIL')
elif (anoDeNascimento >=date.today().year - 19):
    print('JÚNIOR')
elif (anoDeNascimento >=date.today().year - 25):
    print('SÊNIOR')
else:
    print('MASTER')