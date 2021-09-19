"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""


matriz = []

for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        linha.append(valor)
    matriz.append(linha)

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

soma_pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

print(f'A soma dos valores pares é {soma_pares}')

soma_terceira_coluna = 0
for l in range(0, 3):
    soma_terceira_coluna += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')

maior_segunda_linha = 0
for c in range(0, 3):
    if matriz[1][c] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][c]

print(f'O maior valor da segunda linha é {maior_segunda_linha}')