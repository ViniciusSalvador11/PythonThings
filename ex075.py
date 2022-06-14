n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o ultimo número: ')))

print(f'Você digitou os valores {n}')
print(f'O numero nove apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor três apareceu na {n.index(3)+1}ª posição ')
else:
    print('O valor 3 não aparece na tupla')
print('Os valores pares foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')