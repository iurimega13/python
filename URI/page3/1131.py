"""
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).
"""
inter = 0
gremio = 0
empates = 0

while True:
    interGols, gremioGols = map(int, input().split())
    if interGols > gremioGols:
        inter += 1
    elif interGols < gremioGols:
        gremio += 1
    else:
        empates += 1
    
    print("Novo grenal (1-sim 2-nao)")
    resposta = int(input())
    if resposta == 2:
        break


if inter > gremio:
    maiorVencedor = "Inter venceu mais"
elif gremio > inter:
    maiorVencedor = "Gremio venceu mais"
else:
    maiorVencedor = "Nao houve vencedor"

print('{} grenais'.format(inter + gremio + empates))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empates))
print('{}'.format(maiorVencedor))