"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
"""

valores = []

for i in range(10):
    valores.append(int(input()))
    
maior = max(valores)
posicao = valores.index(maior)

print('{}\n{}'.format(maior, posicao))