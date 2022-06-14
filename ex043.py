peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("IMC {:.1f}".format(imc))
    print('Abaixo do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('IMC {:.1f}'.format(imc))
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('IMC {:.1f}'.format(imc))
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('IMC {:.1f}'.format(imc))
    print('Obesidade!')
else:
    print('IMC {:.1f}'.format(imc))
    print('Obesidade mórbida!')