"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a 
média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

media = 0
homemMaisVelho = [0, '']
maisDe20 = 0
for i in range(4):
    print('------- {} pessoa -------'.format(i+1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ')
    media += idade / 4
    if sexo == 'M' and idade > homemMaisVelho[0]:
        homemMaisVelho[0] = idade
        homemMaisVelho[1] = nome
    if idade < 20 and sexo == 'F':
        maisDe20 += 1
print('A média de idade do grupo é {} anos.'.format(media))
print('O homem mais velho tem {} ano(s) e se chama {}.'.format(homemMaisVelho[0], homemMaisVelho[1]) if homemMaisVelho[1] == '' else 'Não há homens no grupo.')
print('Não tem mulheres com menos de 20 anos!' if maisDe20 == 0 else 'Tem {} mulheres com menos de 20 anos.'.format(maisDe20))