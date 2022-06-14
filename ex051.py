pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão da PA: '))
an = pt
dec = pt + (10 - 1) * r
for c in range(pt, dec + r, r):
    print(an, end=' -> ')
    an += r
print('Fim')