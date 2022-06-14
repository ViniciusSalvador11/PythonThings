ano = int(input('Digite o ano de nascimento do atleta: '))
idade = 2022 - ano


if idade <= 9:
    print(idade)
    print('Atleta Mirim!')
elif idade <= 14:
    print(idade)
    print('Atleta Infantil')
elif idade <= 19:
    print(idade)
    print('Atleta Junior!')
elif idade <= 20:
    print(idade)
    print('Atleta Sênior!')
else:
    print(idade)
    print('Atleta Master')