ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    u = int(input('Digite um número entre 0 e 20: '))
    if u > 20 or u < 0:
        u = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if u <= 20 and u >= 0:
            for c in range(u):
                print(f'{ne[u]}')
                break
            if u == 0:
                print(ne[0])
    else:
        for c in range(u):
                print(f'{ne[u]}')
                break
        if u == 0:
            print(ne[0])
    break
