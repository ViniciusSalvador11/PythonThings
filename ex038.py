n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    mv = n1
    print('O maior valor é {}'.format(mv))
elif n2 > n1:
    mv = n2
    print('O maior valor é {}'.format(mv))
else:
    print('Valores iguais')
