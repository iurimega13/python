from math import sqrt

entrada = input().split()
x1 = float(entrada[0])
y1 = float(entrada[1])
entrada = input().split()
x2 = float(entrada[0])
y2 = float(entrada[1])

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('{:.4f}'.format(distancia))