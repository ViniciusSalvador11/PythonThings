import random

derrota =  False
vitorias = 0
while not derrota:
    jog = str(input('Par ou impar? [P/I] ')).strip().capitalize()
    jogn = int(input('Digite um valor entre 0 e 10: '))
    maq = random.randint(0, 10)
    r = jogn + maq
    if jog == 'P':
        if r % 2 == 0:
            derrota = False
            vitorias += 1
            print('-' * 20)
            print(f'Você jogou {jogn} e o computador {maq}. Total de {r} DEU PAR')
            print('-' * 20)
            print('Você ganhou')
        else:
            derrota = True
            print(f'Você jogou {jogn} e o computador {maq}. Total de {r} DEU IMPAR')
            print('-' * 40)
            print('Você perdeu')
    if jog == 'I':
        if not r % 2 == 0:
            derrota = False
            vitorias += 1
            print('-' * 20)
            print(f'Você jogou {jogn} e o computador {maq}. Total de {r} DEU IMPAR')
            print('-' * 40)
            print('Você ganhou')
        else:
            derrota = True
            print('-'*20)
            print(f'Você jogou {jogn} e o computador {maq}. Total de {r} DEU PAR')
            print('-' * 20)
            print('Você perdeu')
#print('Você perdeu')
print('=-'*20)
print(f'GAME OVER! Você venceu {vitorias} vez(es)!')