"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""


pessoas = []
mediaIdade = 0

while True:
    temp = {}
    temp['nome'] = str(input('Nome: '))
    temp['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while temp['sexo'] not in 'MF':
        temp['sexo'] = str(input('Tente novamente! Sexo [M/F]: ')).upper()[0]
    temp['idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('\n','-=-' * 30)
print()

print(' Foram cadastradas {} pessoas!'.format(len(pessoas)))
print('\n','-=-' * 30)
print()

for p in pessoas:
    mediaIdade += p['idade']
mediaIdade /= len(pessoas)

print(' A média de idade é de {} anos.'.format(mediaIdade))
print('\n','-=-' * 30)
print()

mulheresCadastradas = []
for p in pessoas:
    if p['sexo'] == 'F':
        mulheresCadastradas.append(p['nome'])
if len(mulheresCadastradas) == 0:
    print(' Não foram cadastradas mulheres!')
else:
    print(' As mulheres cadastradas foram: ', end='')
    for m in mulheresCadastradas:
        print('{} '.format(m), end='')

print('\n','-=-' * 30)
print()

if len(pessoas) == 1:
    print(' Não foram cadastradas pessoas acima da média de idade!')
else:
    print(' As pessoas acima da média de idade foram: ', end='')
    for p in pessoas:
        if p['idade'] > mediaIdade:
            print(p['nome'], end=' ')
    print()

print('\n','-=-' * 30)