"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8

9
11
13
15
17
19
"""

num = int(input())
count = 0

while True:
    if num % 2 != 0:
        print(num)
        count += 1
    if count == 6:
        break
    num += 1
