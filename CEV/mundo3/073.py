"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

tabela = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Fluminense', 'Atletico-Go', 'Ceará', 'Cuiabá', 'Internacional', 'Juventude', 'Santos', 'São Paulo', 'Bahia', 'America-MG', 'Sport', 'Grêmio', 'Chapecoense')
print('-=-' * 46)
print('Os 5 primeiros times são: {}'.format(tabela[:5]))
print('-=-' * 46)
print('Os últimos 4 colocados são: {}'.format(tabela[-4:]))
print('-=-' * 46)
print('Times em ordem alfabética: {}'.format(sorted(tabela)))
print('-=-' * 46)
print('O time da Chapecoense está na {} posição'.format(tabela.index('Chapecoense') + 1))
print('-=-' * 46)