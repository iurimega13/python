"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numeros = ()

for c in range(0, 4):
    numeros += (int(input(f'Digite o {c+1}º número: ')),)
print('Os números digitados foram {}'.format(numeros))
if 9 in numeros:
    print('O número 9 apareceu {} vezes'.format(numeros.count(9)))
else:
    print('O número 9 não foi digitado')
if 3 in numeros:
    print('O número 3 apareceu na posição {}'.format(numeros.index(3)+1))
else:
    print('O número 3 não foi digitado')

pares = ()
for c in numeros:
    if c % 2 == 0:
        pares += (c,)
print('Os números pares digitados foram {}'.format(pares) if len(pares) > 0 else 'Não foram digitados números pares')