from random import shuffle

alunos = []
i = 1

while(i <= 4):
    alunos.append(input('Digite o nome do {} aluno: '.format(i)))
    i += 1

shuffle(alunos)
print('A ordem dos alunos para apresentação é: {}'.format(alunos))