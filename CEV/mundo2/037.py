valor = int(input('Digite um valor inteiro -» '))
opcao = int(input("""
Escolha uma das base para conversão:

[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL

Sua opção -» """))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a -» {}'.format(valor, bin(valor)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a -» {}'.format(valor, oct(valor)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a -» {}'.format(valor, hex(valor)[2:]))