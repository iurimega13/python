"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2
6 3
5 0

2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""


soma = 0

while True:
    try:
        m, n = map(int, input().split())
        if m > n:
            m, n = n, m
        if m <= 0 or n <= 0:
            break
        for i in range(m, n + 1):
            print(i, end=' ')
            soma += i
        print('Sum={}'.format(soma))
        soma = 0
    except EOFError:
        break