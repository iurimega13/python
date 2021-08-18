m = float(input('Digite a medida em metros: '))

print('Sua medida de metros é: {0} M\n{0} M em centímetros é: {1} cm\n{0} M em milímetros é: {2} mm'.format(
    m,
    (m * 100),
    (m * 1000)
))