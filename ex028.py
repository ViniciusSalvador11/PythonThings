
from random import randint
from time import sleep

numeroCom = randint(0, 5) #nmero sorteado pelo computador
numeroUsu = int(input('Digite um número entre 0 e 5: ')) # número digitado pelo usuario
print('PROCESSANDO...')
sleep(3)
if numeroUsu == numeroCom:
    print('Você acertou! O número sorteado foi {}'.format(numeroCom))
else:
    print('Você errou! O número sorteado foi {}'.format(numeroCom))

