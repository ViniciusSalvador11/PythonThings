lista = list()
numdig = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    r = input('Quer continuar? [s/n ]')
    numdig += 1
    if r != 's':
        break
print('+-'*25)
print(f'Números digitados {numdig}')
print(sorted(lista, reverse=True))
for c, n in enumerate(lista):
    if n == 5:
        print(f'O número 5 apareceu na lista na posição {c}')
    else:
        print('O número 5 não foi digitado')
        break
