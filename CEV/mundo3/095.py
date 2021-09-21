"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogadores = list()

while True:
    jogador = dict()
    
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if jogador['partidas'] == 0:
        print('O jogador não jogou nenhuma partida.')
        jogador['gols'] = 0
        jogador['total de gols'] = 0
    else:
        jogador['gols'] = list()
        for i in range(jogador['partidas']):
            jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    if jogador['partidas'] > 0:
        jogador['total de gols'] = sum(jogador['gols'])
    
    jogadores.append(jogador.copy())
    
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('\n', '-='*30)

print(f'cod nome {"gols":>20}{"total":>22}')
print('-'*60)
for i, jogador in enumerate(jogadores):
    print(f'{i:<3} {jogador["nome"]:<20} {str(jogador["gols"]):<20} {str(jogador["total de gols"]):<20}')
print('-'*60)

while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jogador == 999:
        break
    if jogador >= len(jogadores):
        print('Jogador não encontrado!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[jogador]["nome"].upper()} --')
        for i, gols in enumerate(jogadores[jogador]['gols']):
            print(f'No jogo {i+1} fez {gols} gols.')