mediaidade = 0
maioridade = 0
m21 = 0
for c in range(0, 4):
    print('----------------- {}ª PESSOA ---------------'.format(c+1))
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite a idade : "))
    sexo = str(input('Digite o sexo [M\F]: ')).strip()
    mediaidade += idade
    if sexo.capitalize() == "M":
        if idade >= maioridade:
            maioridade = idade
            maioridaden = nome

    if sexo.capitalize() == "F" and idade < 20:
        m21 += 1
print('A média de idade do grupo é {}.'.format(mediaidade/4))
print('O homem mais velho tem {} e se chama {}.'.format(maioridade, maioridaden))
print('{} mulheres tem menos de 20 anos!'.format(m21))
