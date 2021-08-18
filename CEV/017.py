from math import hypot

print('O valor da hipotenusa é: {:.2f}'.format(
    hypot(
        (float(input('Digite o valor do cateto oposto: '))),
        (float(input('Digite o valor do cateto adjacente: ')))
        )
))