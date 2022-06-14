som = 1
multi = 2
maior = 3
nV = 4
sair = 5
r = 0
while r != 5:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    r = int(input('''Somar [1]
Multiplicar [2]
Maior [3]
Novos Numeros [4]
Sair [5] '''))
    if r == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif r == 2:
        print('{} X {} = {}'.format(v1, v2, v1 * v2))
    elif r == 3:
        if v1 > v2:
            print('O valor {} é maior que {}!'.format(v1, v2))
        else:
            print('O valor {} é maior ou igual que {}!'.format(v2, v1))
    elif r == 4:
        continue
    elif r == 5:
        break
    else:
        print('Opção invalida!')
    print('=-=' * 10)
print('Saiu do programa!')
