from math import hypot

print('O valor da hipotenusa é: {:.2f}'.format(
    hypot(
        (int(input('Digite o valor do cateto oposto: '))),
        (int(input('Digite o valor do cateto adjacente: ')))
        )
))