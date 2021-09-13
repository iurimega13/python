"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                                    
A) quantas pessoas foram cadastradas
B) listagem com as pessoas mais pesadas
C) listagem com as pessoas mais leves
"""

pessoas = list()

while True:
    pessoas.append([str(input('Nome: ')), float(input('Peso: '))])
    
    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Tente novamente. Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    
pessoasMaisPesadas = 0
pessoasMaisLeves = 0

for pessoa in pessoas:
    if pessoa[1] > 80:
        pessoasMaisPesadas += 1
    elif pessoa[1] < 50:
        pessoasMaisLeves += 1

print('Foram cadastradas {} pessoas.'.format(len(pessoas))) 
print('Foram cadastradas {} pessoas mais pesadas (+80).'.format(pessoasMaisPesadas))
print('Foram cadastradas {} pessoas mais leves (-50).'.format(pessoasMaisLeves))