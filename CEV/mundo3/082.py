"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    
    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Tente novamente. Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    
    if valores[-1] % 2 == 0:
        pares.append(valores[-1])
    else:
        impares.append(valores[-1])

print('\nOs valores digitados foram -> {}'.format(sorted(valores)))
print('\nOs valores pares digitados foram -> {}'.format(sorted(pares)))
print('\nOs valores ímpares digitados foram -> {}'.format(sorted(impares)))