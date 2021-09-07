"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

x = termo
i = 1
while i <= 10:
    print(x, end=' --> ')
    x += razao
    i += 1
while True:
    print('PAUSA')
    opcao = int(input('Qunatos termos quer mostrar a mais? '))
    temp = i
    if opcao != 0:
        while i < temp + opcao:
            print(x, end=' --> ')
            x += razao
            i += 1 
    else:
        break
print('Progressão finalizada com {} termos mostrados'.format(i - 1))