idade = int(input('Digite o ano de nascimento: '))
ano = 2022 - idade

if ano < 18:
    print('Idade: {}'.format(ano))
    print('Ainda vai se alistar!')
    print('Faltam {} anos para se alistar!'.format(18-ano))
elif ano == 18:
    print('Idade: {}'.format(ano))
    print('Hora de se alistar!')
else:
    print('Idade: {}'.format(ano))
    print('Não é necessario se alistar!')
    print('Passaram {} anos para se alistar!'.format(ano-18))
