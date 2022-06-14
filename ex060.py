numero = int(input('Digite um numero: '))
contador = numero
fator = 1
print('Calculando {}! = '.format(numero), end="")
while contador > 0:
    print('{} '.format(contador), end='')
    print('X ' if contador > 1 else '= ', end="")
    fator *= contador
    contador -= 1
print('{}'.format(fator))
