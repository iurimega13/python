velo = int(input("Qual a velocidade do carro: "))

if velo > 80:
    print("Você foi multado!")
    multa = (velo - 80) * 7
    print("O valor da multa é de R$ {:.2f}".format(multa))
else:
        print("Tenha um bom dia!")