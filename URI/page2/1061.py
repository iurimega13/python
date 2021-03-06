"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
"""

diaInicio = input().split()
horaInicio = input().split()
diaFim = input().split()
horaFim = input().split()
di, df = int(diaInicio[1]), int(diaFim[1])
hi, mi, si = int(horaInicio[0]), int(horaInicio[2]), int(horaInicio[4])
hf, mf, sf = int(horaFim[0]), int(horaFim[2]), int(horaFim[4])

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = si + mi*minuto_seg + hi*hora_seg + di*dia_seg
f = sf + mf*minuto_seg + hf*hora_seg + df*dia_seg
if i < f:
    tempo = f - i
    dias = int(tempo/dia_seg)
    tempo = tempo%dia_seg
    horas = int(tempo/hora_seg)
    tempo = tempo%hora_seg
    minutos = int(tempo/minuto_seg)
    tempo = tempo%minuto_seg
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))