valorDaCasa = float(input("Digite o valor da casa -»R$ "))
salario = float(input("Digite o salário do comprador -»R$ "))
anos = int(input("Digite em quantos anos ele vai pagar -» "))

prestação = valorDaCasa / (anos * 12)
if (prestação > salario * 0.3):
    print("O valor da prestação é de R$ {:.2f}".format(prestação))
    print("O comprador não pode pagar a prestação")
else:
    print("O comprador pode pagar as pretações\nValor da prestação -»R$ {:.2f}".format(prestação))