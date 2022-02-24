dA = int(input('Quantos dias alugados? '))
km = float(input('Quantos Kms rodados? '))
a = (dA * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(a))
