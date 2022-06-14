N = int(input('Digite um numero: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
esc = int(input('Sua opção: '))

if esc == 1:
    print('{} convertido para BINARIO é igual a {}'.format(N, bin(N)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é igual a {} '.format(N, oct(N)[2:]))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(N, hex(N)[2:]))
else:
    print('Digitou uma opção não disponivel!')