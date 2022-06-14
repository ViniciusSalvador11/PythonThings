import random

print('''[ 1 ] Pedra
[ 2 ] Papel 
[ 3 ] Tesoura''')
jogador = int(input('Escolha seu proximo ataque: '))
maquina = random.randrange(1, 3, 1)
print(maquina)
if jogador == 1 and maquina == 3:
    print('Maquina jogou tesoura!')
    print('Jogador venceu da maquina!')
elif maquina == 1 and jogador == 3:
    print('Maquina jogou pedra!')
    print('Maquina venceu do jogador!')
elif jogador == 2 and maquina == 1:
    print('Maquina jogou pedra!')
    print('Jogador ganhou da maquina!')
elif maquina == 2 and jogador == 1:
    print('Maquina jogou papel!')
    print('Maquina ganhou do jogador!')
elif jogador == 3 and maquina == 2:
    print('Maquina jogou papel!')
    print('Jogador ganhou da maquina!')
elif maquina == 3 and jogador == 2:
    print('Maquina jogou tersoura!')
    print('Jogador ganhou do jogador!')
elif jogador == maquina:
    print('Empate!')
else:
    print('Opção invalida')
