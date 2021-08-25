"""
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

qtdVAlores = 0
somaValores = 0

for i in range(1, 501):
    if i % 3 == 0:
        qtdVAlores += 1
        somaValores += i
print(f'A soma dos {qtdVAlores} valores solicitados é {somaValores}')