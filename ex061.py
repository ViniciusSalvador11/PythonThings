print('Gerador de PA')
print('-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end="")
    termo = termo + razao
    cont += 1

print('Fim')
