from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #tem de ser divisivel por 4, não divisivel por 100 ou não divisivel por 400
    print('{} é BISSEXTO!'.format(ano))
else:
    print('{} não é BISSEXTO!'.format(ano))
