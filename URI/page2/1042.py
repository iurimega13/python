"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
Entrada
A entrada contem três números inteiros.
Saída
Imprima a saída conforme foi especificado.
Exemplo de Entrada	Exemplo de Saída
7 21 -14
-14
7
21
7
21
-14
"""

valor1, valor2, valor3 = map(int, input().split())
ordenado = sorted([valor1, valor2, valor3])
print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(ordenado[0], ordenado[1], ordenado[2], valor1, valor2,valor3))