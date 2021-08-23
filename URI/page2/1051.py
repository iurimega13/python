valor = float(input())

ir1 = (valor - 2000) * 0.08
ir2 = (valor - 3000) * 0.18 + (1000 * 0.08)
ir3 = (valor - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)

if valor <= 2000:
    print("Isento")
elif valor <= 3000:
    print('R$ {:.2f}'.format(ir1))
elif valor <= 4500:
    print('R$ {:.2f}'.format(ir2))
else:
    print('R$ {:.2f}'.format(ir3))