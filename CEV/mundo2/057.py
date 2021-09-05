"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja 
errado, peça a digitação novamente até ter um valor correto.
"""

sexo = input('Informe seu sexo: [M/F] ').upper()
while True:
    if sexo == 'M':
        print('Sexo Masculino registrado com sucesso!')
        break
    elif sexo == 'F':
        print('Sexo Feminino registrado com sucesso!')
        break
    else:
        sexo = input('Dados inválidos. Por favor, informe seu sexo: [M/F] ').upper()
    