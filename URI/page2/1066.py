"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
Exemplo de Entrada	Exemplo de Saída
-5
0
-3
-4
12
3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
"""

par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par, impar, positivo, negativo))