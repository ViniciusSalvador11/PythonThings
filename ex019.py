
import random

aluno1 = input('Digite o nome: ')
aluno2 = input('Digite o nome: ')
aluno3 = input('Digite o nome: ')
aluno4 = input('Digite o nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print('O escolhido foi {}'.format(sorteado))


