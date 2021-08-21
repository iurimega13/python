from random import randint
from time import sleep

cpu = randint(1, 5)

print("-=-" * 20)
print("Vou pensar em um número entre 1 e 5. Tente adivinhar...")
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
    i += 1
if i >= 3:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(cpu, palpite))
