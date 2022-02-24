pa = float(input('Digite a altura da sua parede em metros: '))
pl = float(input('Digite a largura da sua parede em metros: '))
a = pa * pl
print(a, 'm² de área')
print('Você precisará de {} litros de tinta para pintar a parede'.format(a/2))

