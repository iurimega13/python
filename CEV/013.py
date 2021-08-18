salario = float(input('Digite seu salário: R$ '))
print('Seu salario com 15% de aumento é: R$ {:.2f}'.format(
    (salario + (salario * 0.15))
))