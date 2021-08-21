"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""

compras = float(input("Digite o valor da compra: "))

opcao = int(input("""
Digite a opção de pagamento:

[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão

Opção -» """))

if opcao == 1:
    print("Valor da compra com 10% de desconto: R$ {:.2f}".format(compras - (compras * 0.1)))
elif opcao == 2:
    print("Valor da compra com 5% de desconto: R$ {:.2f}".format(compras - (compras * 0.05)))
elif opcao == 3:
    print("Valor da compra com preço formal: R$ {:.2f}".format(compras))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(parcelas, (compras +(compras * 0.2)) / parcelas))
else:
    print("Opção inválida")