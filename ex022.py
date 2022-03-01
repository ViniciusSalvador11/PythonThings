nome = str(input('Digite seu nome e sobrenome: ')).strip()
primeiroN = nome.split()
print('Seu nome em maiusculas é', nome.upper())
print('Seu nome em minusculas é', nome.lower())
print('Seu nome tem ao todo', len(nome)-nome.count(' '))
print('Seu primeiro nome tem ao todo', len(primeiroN[0]))


