n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('MÉDIA {:.2f}'.format(media))
    print('REPROVADO!')
elif media >= 5 and media < 7:
    print('MÉDIA {:.2f}'.format(media))
    print('RECUPERAÇÃO!')
else:
    print('MÉDIA {:.2f}'.format(media))
    print('APROVADO!')