"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""


valores = [[], []]

for i in range(1, 8):
    num = int(input('Digite {}º número: '.format(i)))
    
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('-=' * 40)

print('Os valores pares digitados foram: {}\n'.format(sorted(valores[0])))
print('Os valores ímpares digitados foram: {}'.format(sorted(valores[1])))