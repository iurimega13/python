"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

valores = []

for i in range(0, 5):
    valor = int(input('Digite o {}º valor: '.format(i+1)))
    
    if i == 0:
        valores.append(valor)
        print('O valor {} foi adicionado ao final da lista...'.format(valor))
    else:
        for j in range(0, len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                print('O valor {} foi adicionado na posição {}...'.format(valor, j+1))
                break
            elif j == len(valores)-1:
                valores.append(valor)
                print('O valor {} foi adicionado ao final da lista...'.format(valor))
                break
print('-='*40)
print('Os valores digitados em ordem foram: {}'.format(valores))