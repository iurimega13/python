from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo: '))

print('O valor do seno é: {:.2f}\nO valor do coseno é: {:.2f}\nO valor da tangente é: {:.2f}'.format(
    sin(radians(angulo)),
    cos(radians(angulo)),
    tan(radians(angulo))
))