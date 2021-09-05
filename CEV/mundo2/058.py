"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

cpu = randint(1, 10)

print("-=-" * 20)
print("Vou pensar em um número entre 1 e 10. Tente adivinhar...")
print("-=-" * 20)

i = 1
while i <= 3:
    print("Tentativa {} de 3".format(i))
    palpite = int(input("Em que número eu pensei? "))
    print("PROCESSANDO...")
    sleep(1)
    if palpite == cpu:
        print("PARABÉNS! Você conseguiu me vencer!")
        i = 1
        break
    print('Errou!!')
    i += 1
else:
    print("GANHEI! Eu pensei no número {}!".format(cpu, palpite))
