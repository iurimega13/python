"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""

def titulo(txt):
    print('-=-' * 20)
    print('{}'.format(txt.center(40)))
    print('-=-' * 20)
    
def pydoc(comando):    
    help(comando)

def pyhelp():
    titulo('PyHelp')
    while True:
        comando = str(input('Função ou Biblioteca > '))
        if comando.upper() == 'FIM':
            break
        else:
            pydoc(comando)
    print('\nObrigado por usar o PyHelp!')

pyhelp()