numeros = list()
maiorn = 0
menorn = 999999999999999999999999999999999999999999
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {c+1}: ')))
    for c, n in enumerate(numeros):
        if n > maiorn :
            maiorn = n
            maiorc = c
        elif n < menorn:
            menorn = n
            menorc = c
print(f'O menor número foi {menorn} encontrado na posição {menorc+1}')
print(f'O maior número foi {maiorn} encontrado na posição {maiorc+1}')

