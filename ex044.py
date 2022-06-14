vp = float(input('Preço da Compra: '))
print('[ 1  ]À vista no dinheiro')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Em até 2 vezes no cartão')
print('[ 4 ] 3 ou mais vezes no cartão')
esc = int(input('Escolha a forma de pagamento: '))


if esc == 1:
    vf = vp - (0.10 * vp)
    print('Recebeu um desconto de 10%! Novo valor: R${}'.format(vf))
elif esc == 2:
    vf = vp - (0.05 * vp)
    print('Recebeu um desconto de 5%! Novo valor: R${}'.format(vf))
elif esc == 3:
    vf = vp/2
    print('{} Parcelas de R${}'.format(2, vf))
elif esc == 4:
    vf = (0.20 * vp) + vp
    pc = int(input('Quantas parcelas ? '))
    p = vf/pc
    print('Juros de 20%! Novo valor total de R${} e {} parcelas de R${}'.format(vf, pc, p))
else:
    print('Opção invalida! Tente novamente')
