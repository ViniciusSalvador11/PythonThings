lista = ('pão', 6, 'agua', 3, 'lapis', 2.50, 'borracha', 1.50, 'chocolate', 2.55)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>5.2f}')
print('-'*40)