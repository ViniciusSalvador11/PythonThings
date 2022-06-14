nd = 0
n = 1
s = 0

while n != 999:
    n = int(input('Digite um número: [999 para parar]'))
    if n != 999:
        nd += 1
        s += n
print(f'Foram digitados {nd} números e a soma deles foi {s}!')
