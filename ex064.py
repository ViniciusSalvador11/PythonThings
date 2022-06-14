r = 0
s = 0
nd = 0
while r != 999:
    r = int(input('Digite um número [999 para sair]: '))
    nd += 1
    if r != 999:
        s += r
print('Foram digitados {} números com o total de {}.'.format(nd - 1, s))
