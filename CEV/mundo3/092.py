"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

anoAtual = date.today().year
trabalhador = {}

trabalhador['nome'] = input('Nome: ')

anoDeNascimento = int(input('Ano de Nascimento: '))
trabalhador['idade'] = anoAtual - anoDeNascimento

numeroDaCarteira = int(input('Número da Carteira de Trabalho (0 não tem): '))

if numeroDaCarteira != 0:
    trabalhador['ctps'] = numeroDaCarteira
    anoDeContratacao = int(input('Ano de Contratação: '))
    trabalhador['contratacao'] = anoDeContratacao
    salario = float(input('Salário: R$ '))
    trabalhador['salario'] = salario
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['contratacao'] + 35) - anoAtual
    
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor --> {v}')
if numeroDaCarteira == 0:
    print('  - O trabalhador não possui carteira de trabalho')