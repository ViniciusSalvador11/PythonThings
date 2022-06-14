
resposta = 'S'
m20 = 0
p18 = 0
h = 0
while resposta == 'S'.capitalize():
    print("-"*20)
    print(' CADASTRE UMA PESSOA ')
    print('-'*20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().capitalize()

    if sexo == 'F'.capitalize() and idade <= 20:
        m20 += 1
    if idade >= 18:
        p18 += 1
    if sexo == 'M'.capitalize():
        h += 1
    resposta = str(input('Quer continuar? [S/N] ')).capitalize()
print('======== FIM DO PROGRAMA ============')
print(f'Total de pessoas com mais de 18 anos: {p18}')
print(f'Ao todo temos {h} homem(ns) cadastrados')
print(f'E temos {m20} mulher(es) com menos de 20 anos')
