"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
Entrada
Leia três valores de ponto flutuante (double) A, B e C.
Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
Exemplos de Entrada	Exemplos de Saída
10.0 20.1 5.1
R1 = -0.29788
R2 = -1.71212
0.0 20.0 5.0
Impossivel calcular
"""

a, b, c = map(float, input().split())

if a == 0:
    print('Impossivel calcular')
elif (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    r1 = (-b + ((b ** 2 - 4 * a * c)) ** 0.5) / (2 * a)
    r2 = (-b - ((b ** 2 - 4 * a * c)) ** 0.5) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))