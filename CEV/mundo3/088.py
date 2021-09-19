"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint

palpites = []

numeroDeJogos = int(input('Quantos jogos você quer fazer? '))

for i in range(numeroDeJogos):
    jogos = []
    for j in range(6):
        numero = randint(1, 60)
        while numero in jogos:
            numero = randint(1, 60)
        jogos.append(numero)
    palpites.append(jogos)

print(f'\n{"-=" * 20}')

for i, j in enumerate(palpites):
    print(f'Jogo {i+1}: {sorted(j)}')