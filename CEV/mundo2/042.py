print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

lado1 = float(input('Primeiro segmento -> '))
lado2 = float(input('Segundo segmento -> '))
lado3 = float(input('Terceiro segmento -> '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES!')
    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')