resposta = 'S'
gasto = 0
maior1000 = 0
menor = 99999999
print('-'*40)
print('Loja Super Barato')
print('-'*40)
while resposta == 'S'.capitalize():
    nomeP = str(input('Digite o nome do produto: '))
    precoP = float(input('Digite o preço do produto: R$ '))
    gasto += precoP
    if precoP >= 1000:
        maior1000 += 1
    if precoP < menor:
        menorN = nomeP
        menor = precoP
    resposta = str(input('Quer continuar? [S/N ]')).capitalize()
print('------------ FIM DO PROGRAMA --------------')
print(f'O total da compra foi R${gasto:.2f}')
print(f'Temos {maior1000} produtos  custando mais que R$1000.00')
print(f'O produto mais barato foi {menorN} que custa R${menor:.2f}')
