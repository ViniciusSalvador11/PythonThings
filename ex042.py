print('-='*20)
print('ANALISADOR  DE TRIÃNGULOS')
print('-='*20)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo ', end='')
    if r1 == r2 and r1 == r3 and r3 == r2:
        print('Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isósceles!')
    elif r1 != r2 and r1 != r3 and r3 != r2:
        print('Escaleno')
else:
    print('Não é possivel formar um triangulo!')