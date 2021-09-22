"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

def titulo(msg):
    print('\033[1;30m-=' * 20)
    print('\033[1;30m{}\033[m'.format(msg.center(40)))
    print('-=' * 20)


def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            break
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


titulo('Leia Inteiro')

print('O número digitado foi {}'.format(leiaInt()))