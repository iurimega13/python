"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    n = int(input("Digite um número para ver sua tabuada: "))
    if n < 0:
        break
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n*i))
    print()