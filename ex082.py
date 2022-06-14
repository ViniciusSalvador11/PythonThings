listaprimaria = list()
listapar = list()
listaimpar = list()
while True:
    listaprimaria.append(int(input('Digite um número: ')))
    r = input('Quer continuar? [s/n] ')
    if r != 's':
        break

for n in listaprimaria:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

print(f'A lista com todos os numeros é {listaprimaria}')
print(f'Somente númeors pares da lista {listapar}')
print(f'Somente números impares da lista {listaimpar}')
