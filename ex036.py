ValorCasa = float(input('Qual o valor da casa? '))
Salario = float(input('Qual o seu salario? '))
Anos = int(input('Em quantos anos pretende pagar? '))
PS = Salario * 0.30
prestaçao = ValorCasa / (Anos * 12)

if prestaçao <= PS:
    print('Aprovado! Abaixo de 30% do salario, que é R${:.2f}'.format(PS))
    print('Prestação R${:.2f}'.format(prestaçao))
else:
    print('Não aprovado! Acima de 30% do salario, que é  R${:.2f}'.format(PS))
    print('Prestação R${:.2f}'.format(prestaçao))
