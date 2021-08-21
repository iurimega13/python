dias = int(input('Digite quantos dias o carro ficou alugado: '))
km = float(input('Digite quantos km o carro percorreu: '))

print('R$ {:.2f} pelos dias\nR$ {:.2f} pelos km\nTotal a pagar pelo aluguel R$ {:.2f}'.format(
    (dias * 60),
    (km * 0.15),
    ((dias * 60)+ (km * 0.15))
))