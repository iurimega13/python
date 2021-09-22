"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def titulo(txt):
    """
    :param txt: texto a ser impresso com o titulo
    retorna o texto com formatação de titulo
    """
    print('-' * 40)
    print(txt)
    print('-' * 40)


def ficha(jogador='<desconhecido>', gols=0):
    """
    :param jogador: nome do jogador
    :param gols: quantidade de gols marcados
    :print: imprime a ficha do jogador
    """
    print('O jogador {} fez {} gol(s) no campeonato.'.format(jogador, gols))
    
    
titulo('Ficha de jogador')
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if jogador.strip() == '':
    jogador = '<desconhecido>'
if gols.strip() == '':
    gols = 0
ficha(jogador, int(gols))