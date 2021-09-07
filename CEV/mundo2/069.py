"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

totalMais18 = 0
homensCadastrados = 0
mulheresMenos20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        totalMais18 += 1
    if sexo == 'M':
        homensCadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print("""
Total de pessoas com mais de 18 --> {}
Total de homens cadastrados --> {}
Total de mulheres com menos de 20 cadastradas --> {}""".format(totalMais18, homensCadastrados, mulheresMenos20))