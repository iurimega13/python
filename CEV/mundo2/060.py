"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

n = int(input('Digite um número para calcular seu fatorial --> '))

i = n
fatorial = str(n)
result = n
for i in range(n - 1, 0, -1):
    fatorial +=  ' x ' + str(i)
    result *= i 
    i -= 1
print('{}! = {} = {}'.format(n, fatorial, result))