distancia = int(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    preco = distancia * 0.50
    print("O preço da sua passagem será de R${:.2f}".format(preco))
else:
    preco = distancia * 0.45
    print("O preço da sua passagem será de R${:.2f}".format(preco))
