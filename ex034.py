salario = float(input('Digite o salario do funcionario: '))
if salario <= 1.250:
    nsalario = (0.15 * salario) + salario
    print('O novo salario é R$ {:.2f}'.format(nsalario))
else:
    nsalario = (0.10 * salario) + salario
    print('O novo salario é de R$ {:.2f}'.format(nsalario))
