from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
print('\n=> JOKENPO\n')
a = '-'*30
empate = derrota = vitoria = partida = 0
def jokenpo():
    jok = ['JO', 'KEN','PÔ!']
    for c in range(0, 3):
        print(f'{jok[c]} ', end='', flush=True)
        sleep(1/2)
    print(f'\n{a}') 
    print(f'PC: Eu joguei {itens[computador]} e você {itens[jogada]}.')
def vitoria_1():
    jokenpo()
    print('          Você ganhou!')
    print('-'*30)
def derrota_1():
    jokenpo()
    print('          Você perdeu!')
    print('-'*30) 
def zerar():
    empate = derrota = vitoria = partida = 0
    sleep(1)
def partidas():
    print(f'\n   {partida} partidas jogadas.')
    print(f'\nPC: Eu venci {derrota} vez(es) e você {vitoria} vez(es). Empatamos {empate} vez(es).')
def jogofin():
    print('-'*30)
    sleep(2)
    print('Jogo sendo finalizado...')
    sleep(1/2)
while True:
    while True:
        computador = randint(0, 2)
        partida += 1
        if partida == 3:
            print(f'PARTIDA {partida} - FINAL')
        elif partida >= 2:
            print(f'PARTIDA {partida}')
        elif partida == 1:
            print('-'*9)
            print(f'PARTIDA {partida}')
        print('[0] Pedra\n[1] Papel\n[2] Tesoura')
        while True:
            try:
                jogada = int(input('Sua jogada: '))
                break
            except ValueError:
                print('PC: Valor digitado inválido. Digite as opções númericas.')
        while jogada > 2:
            jogada = int(input('PC: Valor digitado inválido. Digite as opções númericas válidas.\nSua jogada: '))
        if jogada == computador:
            empate += 1
            jokenpo()
            print('             EMPATE')
            print('-'*30)
        elif jogada == 0 and computador == 1:
            derrota += 1
            derrota_1()
        elif jogada == 0 and computador == 2:
            vitoria += 1
            vitoria_1()
        elif jogada == 1 and computador == 0:
            vitoria += 1
            vitoria_1()
        elif jogada == 1 and computador == 2:
            derrota += 1
            derrota_1()
        elif jogada == 2 and computador == 1:
            vitoria += 1
            vitoria_1()
        elif jogada == 2 and computador == 0:
            derrota += 1
            derrota_1()
        if partida >= 3:
            break
    np = input('PC: Você deseja continuar? [S/N]: ').strip().upper()
    sleep(0.5)
    if np in 'S':
            continue
    elif np in 'N':
        if derrota > vitoria:
            partidas()
            sleep(1)
            print('PC: Você perdeu! Foi uma ótima partida, talvez na próxima você ganhe...')
            jogofin()
            break
        elif derrota < vitoria:
            partidas()
            sleep(1)
            print('PC: Você ganhou!! Talvez na próxima eu ganhe :)...')
            jogofin()
            break
        elif derrota == vitoria:
            partidas()
            sleep(1)
            print('PC: Nós empatamos! Parece que nós dois somos muito bons, quero revanche hein.')
            jogofin()
            break 
    while np not in 'SN' :
        np = input('PC: Digite uma opção válida.\nPC: Você deseja continuar? [S/N]: ').strip().upper()
