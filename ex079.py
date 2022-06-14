lista = list()
primd = 0
ultmd = 0
while True:
    n = int(input('Digite um numero: '))
    ultmd = n
    r = input("Quer continuar? [s/n] ")
    if r != 's':
        break

    if n > ultmd and n > primd:
        lista.append(n)
        ultmd  = n
    elif n < ultmd and n < primd:
        lista.__add__(n)


print(lista)