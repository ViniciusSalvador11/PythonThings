cidade = str(input('Digite o nome de uma cidade: ')).strip()
dividido = cidade.split()
if dividido[0].capitalize().find('Santo') == False:
    print('A cidade começa com o nome Santo')
else:
    print('A cidade  não começa com o nome Santo')
