from datetime import date

atual = date.today().year
m = 0
n = 0

for c in range(0, 7):
    a = int(input('Em que ano a {}ª pessoa nasceu: '.format(c+1)))
    idade = atual - a
    if idade <= 21:
        n += 1
    else:
        m += 1
print('{} pessoa(s) ainda é(são) menor(es) de idade e {} já é(são) de maior!'.format(n, m))
