""""
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

peso = float(input("Digite o seu peso: (Kg) "))
altura = float(input("Digite sua altura: (m) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Peso Ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")