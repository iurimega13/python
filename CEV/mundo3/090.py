"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))

print('-=-' * 30)

print(' - Nome: {}'.format(aluno['nome']))
print(' - Média: {:.1f}'.format(aluno['media']))

if aluno['media'] >= 7:
    print(' - Situação: Aprovado')
elif aluno['media'] >= 5:
    print(' - Situação: Recuperação')
else:
    print(' - Situação: Reprovado')