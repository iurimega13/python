from random import choice

alunos = []
i = 1

while(i <= 4):
    alunos.append(input('Digite o nome do {} aluno: '.format(i)))
    i += 1

print('O aluno escolhido foi: {}'.format(choice(alunos)))