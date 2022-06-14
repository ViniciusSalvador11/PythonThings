s = str(input('Digite o seu sexo: [M/F] ')).strip()
while s != 'm' and s != 'f':
    if s != 'm' and s != 'f':
        print('Digite um sexo valido!')
        s = str(input('Digite o seu sexo: [M/F] ')).strip()
if s == 'm':
    print('O seu sexo é Masculino')
else:
    print('O seu sexo é Feminino')
