import math

co = float(input("Digite o cateto oposto: "))
ca = float(input('Digite o cateto adjacente: '))
h = ca**2 + co**2
hipc = math.sqrt(h)
print(h)
print('Comprimento da hipotenusa: {:.2f}'.format(hipc))
