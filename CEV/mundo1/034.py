salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)

print('O novo salário do funcionário é de R$ {:.2f}'.format(novo_salario))