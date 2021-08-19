peca1 = input()
peca2 = input()

peca1 = peca1.split()
peca2 = peca2.split()

total = (float(peca1[1]) * float(peca1[2]))+(float(peca2[1]) * float(peca2[2]))

print('VALOR A PAGAR: R$ {}'.format(total))