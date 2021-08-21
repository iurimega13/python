from random import choice
from time import sleep
jokken = ['pedra', 'papel', 'tesoura']

cpu = choice(jokken)

opcao = int(input("""
\033[1;30;40m -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                     JOKKENPÔ                        
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
 |          ESCOLHA UMA DAS OPÇOES ABAIXO           |
 |   [1] PEDRA                                      |
 |                                                  |
 |   [2] PAPEL                                      |
 |                                                  |
 |   [3] TESOURA                                    |
 |                                                  |
 |__________________________________________________|
 
     SUA OPÇÃO ---> \033[m"""))
jogador = jokken[opcao - 1]

sleep(1)
print('\033[1;30;40m     JO')
sleep(1)
print('\033[1;30;40m     KEN')
sleep(1)
print('\033[1;30;40m     PÔ!!!')

if cpu == 'pedra' and jogador == 'pedra' or cpu == 'tesoura' and jogador == 'tesoura' or cpu == 'papel' and jogador == 'papel':
    print('''\033[1;30;40m 
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                     RESULTADO
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                                                     
       CPU ESCOLHEU -» {}                            
       VOCÊ ESCOLHEU -» {}                           
                                                     
 |--------------------------------------------------|
 |                                                  |
 |               !!!! EMPATOU !!!!                  |
 |                                                  |
 |__________________________________________________|\033[m'''.format(cpu.upper(), jogador.upper()))
elif cpu == 'tesoura' and jogador == 'pedra' or cpu == 'papel' and jogador == 'tesoura' or cpu == 'pedra' and jogador == 'papel':
    print('''\033[1;30;40m 
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                     RESULTADO
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                                                     
       CPU ESCOLHEU -» {}                            
       VOCÊ ESCOLHEU -» {}                           
                                                     
 |--------------------------------------------------|
 |                                                  |
 |             !!!! VOCÊ VENCEU !!!!                |
 |                                                  |
 |__________________________________________________|\033[m'''.format(cpu.upper(), jogador.upper()))
else:
    print('''\033[1;30;40m 
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                     RESULTADO
 -==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
                                                     
       CPU ESCOLHEU -» {}                            
       VOCÊ ESCOLHEU -» {}                           
                                                     
 |--------------------------------------------------|
 |                                                  |
 |             !!!! VOCÊ PERDEU !!!!                |
 |                                                  |
 |__________________________________________________|\033[m'''.format(cpu.upper(), jogador.upper()))