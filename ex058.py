from random import randint
from time import sleep

numeroCom = randint(0, 10) #nmero sorteado pelo computador

tU = 0
acertou = False
#print('PROCESSANDO...')
#sleep(3)
while not acertou:
    numeroUsu = int(input('Digite um número entre 0 e 10: '))  # número digitado pelo usuario
    tU += 1
    if numeroUsu == numeroCom:
        acertou = True

    else:
        if numeroUsu < numeroCom:
            print('Mais...')
        elif numeroUsu > numeroCom:
            print('Menos...')

print('Acertou com {} tentativas. Parabéns!'.format(tU))
