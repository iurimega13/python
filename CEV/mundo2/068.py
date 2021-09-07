"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random
vitoriasConsecutivas = 0
while True:
    palpites = ['P', 'I']
    cpuPalpite = random.choice(palpites)
    cpuValor = random.randint(1, 10)
    
    jogadorPalpite = input('Digite [P] para par ou [I] para ímpar: ').upper()
    jogadorValor = int(input('Digite um valor de 1 a 10: '))
    
    if (cpuValor % 2 == 0 and jogadorPalpite == 'P' or cpuValor % 2 != 0 and jogadorPalpite == 'I') and (jogadorValor % 2 == 0 and cpuPalpite == 'P' or jogadorValor % 2 != 0 and cpuPalpite == 'I') or (cpuValor % 2 == 0 and jogadorPalpite == 'I' or cpuValor % 2 != 0 and jogadorPalpite == 'P') and (jogadorValor % 2 == 0 and cpuPalpite == 'I' or jogadorValor % 2 != 0 and cpuPalpite == 'P'):
        print("""
Empate!!!
Você jogou {} e o computador jogou {}.
Seu palpite foi {} e do computador {}.""".format(jogadorValor, cpuValor, jogadorPalpite, cpuPalpite))
        vitoriasConsecutivas = 0
    elif cpuValor % 2 == 0 and jogadorPalpite == 'P' or cpuValor % 2 != 0 and jogadorPalpite == 'I':
        vitoriasConsecutivas += 1
        print('')
        print('''
Você ganhou!!!
Você jogou {} e o computador {}.
Seu palpite foi {} e do computador {}
Total de {} de vitórias consecutivas.'''.format(jogadorValor, cpuValor, jogadorPalpite, cpuPalpite, vitoriasConsecutivas))
    else:
        print("""
Derrota!!!
Você jogou {} e o computador jogou {}.
Seu palpite foi {} e do computador {}.
Total de {} de vitórias consecutivas.""".format(jogadorValor, cpuValor, jogadorPalpite, cpuPalpite, vitoriasConsecutivas))
        break