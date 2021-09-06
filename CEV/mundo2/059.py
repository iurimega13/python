"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

while True:
    opcao = int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

O que deseja fazer »»» """))
    if opcao == 1:
        print('A soma entre {} e {} é: {}'.format(v1, v2, v1 + v2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é: {}'.format(v1, v2, v1 * v2))
    elif opcao == 3:
        print('O maior número entre {} e {} é: {}'.format(v1, v2, max(v1, v2)))
    elif opcao == 4:
        print('Digite os novos valores!')
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        break
    else:
        print('Opção inválida!!\nTente novamente!!')