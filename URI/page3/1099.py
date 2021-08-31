"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	Exemplo de Saída
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8
0
11
5
0
0
0
12
"""

n = int(input())
somados =  []
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    soma = 0
    for j in range(x + 1, y):
        if j % 2 != 0:
            soma += j
    somados.append(soma)
print("\n".join(map(str, somados)))
