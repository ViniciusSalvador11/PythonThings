distancia = int(input('Digite a distância da viagem em KM: '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem do ônibus é R$ {:.2f}!!!'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da passagem do ônibus é R$ {:.2f}!!!'.format(preco))
