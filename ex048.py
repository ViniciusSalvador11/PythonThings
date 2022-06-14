s = 0
cont = 0
for c in range(1, 500+1):
    if not c % 2 == 0 and c % 3 == 0:
        print(c)
        s += c
        cont += 1
print('A soma dos {} valores impares e multiplos de três é {}'.format(cont, s))

