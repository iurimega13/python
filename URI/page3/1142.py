"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
"""
n = int(input())

a,b,c = 1,2,3

for i in range(n):
    print('{} {} {} PUM'.format(a,b,c))
    a += 4
    b += 4
    c += 4