"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
Saída
Apresente a duração do jogo conforme exemplo abaixo.
Exemplo de Entrada	Exemplo de Saída
16 2
O JOGO DUROU 10 HORA(S)
0 0
O JOGO DUROU 24 HORA(S)
2 16
O JOGO DUROU 14 HORA(S)
"""

horaInicial, horaFinal = map(int, input().split())
i = horaInicial
duracao = 0
while True:
    if i == 24:
        i = 0
        duracao += 1
    else:
        i += 1
        duracao += 1
        
    if i == horaFinal:
        break
if horaInicial == horaFinal:
    print("O JOGO DUROU 24 HORA(S)")
else:   
    print('O JOGO DUROU {} HORA(S)'.format(duracao - 1) if horaInicial > horaFinal else 'O JOGO DUROU {} HORA(S)'.format(duracao))