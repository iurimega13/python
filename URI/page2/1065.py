"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
Exemplo de Entrada	Exemplo de Saída
7
-5
6
-4
12
3 valores pares
"""

pares = 0

for i in range(5):
    if int(input()) % 2 == 0:
        pares += 1
print("{} valores pares".format(pares))