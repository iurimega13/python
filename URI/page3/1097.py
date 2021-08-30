"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
"""

i = 1
j = 7
while True:
    temp = j
    for n in range(3):
        print('I={} J={}'.format(i, temp))
        temp -= 1
    j += 2
    i += 2
    if i > 9:
        break