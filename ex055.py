map = 0
mep = 0
for c in range(0, 5):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if p == 1:
        map = p
        mep = p
    else:
        if p > map:
            map = p
        if p < map:
            mep = p
print('O maior peso digitado foi {}Kg e o menor foi {}Kg'.format(map, mep))
