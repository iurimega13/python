x = int(int(input('Quanto de dinheiro você tem na carteira: R$ ')))

print('Com R$ {} você pode comprar US$ {:.2f}'.format(
    x,
    (x / 5.37)
))