rc = 0
m = 0
soma = 0
nd = 0
maior = 0
menor = 999999
while rc != 'N':
    r = int(input('Digite um número: '))
    nd += 1
    soma += r
    if r > maior:
        maior = r
    if r < menor:
        menor = r
    rc = str(input('Quer continuar? [S/N]')).capitalize().strip()
print('A média dos numeros digitados foi {}'.format(soma/nd))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))
