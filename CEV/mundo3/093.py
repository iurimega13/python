"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

if jogador['partidas'] == 0:
    print('O jogador não jogou nenhuma partida.')
else:
    jogador['gols'] = list()
    for i in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['total de gols'] = sum(jogador['gols'])

print('\n','-=' * 30)
print(jogador)
print('\n','-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('\n','-=' * 30)
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print('Foi um total de {} gols'.format(jogador['total de gols']))
print('\n','-=' * 30)