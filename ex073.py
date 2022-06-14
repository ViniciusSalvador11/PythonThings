tabela = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro',
          'Botafogo', 'Santos', 'Fluminense', 'Coritiba', 'América',
          'Avai', 'Internacional', 'Athletico PR', 'Bragantino',
          'Flamengo', 'Goias', 'Cuiaba', 'Atletico GO',
          'Juventude', 'Ceara', 'Fortaleza')

print(f'Os primeiros cinco colocados {tabela[:5]}')
print('-'*100)

print(f'Os quatro ultimos são {tabela[16:]}')

print('-'*100)
print('Ordenado: ')
print(sorted(tabela))
print('-'*100)
bragantino = tabela.index('Bragantino') + 1
print(f'O Bragantino esta na {bragantino}ª posição.')



