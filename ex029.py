velocidade = float(input('Digite a velocidade de um carro: '))
if velocidade > 80:
    print('Você ultrapassou a velocidade maxima!')
    multa = (velocidade - 80) * 7.0
    print('A sua multa é de R$ {:.2f}!'.format(multa))
else:
    print('Você não ultrapassou a velocidade maxima :)')