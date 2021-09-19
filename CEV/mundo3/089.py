"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []

while True:
    aluno = []
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    alunos.append(aluno[:])
    
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{(aluno[1]+aluno[2])/2:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        break
    elif opcao >= len(alunos):
        print('Aluno inexistente!')
    else:
        print('\n', '-=' * 30)
        print(f'\n    Notas de {alunos[opcao][0]} são --> {alunos[opcao][1]} e {alunos[opcao][2]}')
        print('\n', '-=' * 30)