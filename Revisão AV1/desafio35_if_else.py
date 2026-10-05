print('Vamos verificar se três retas formam um triângulo!')

lado1 = float(input('Digite o comprimento da 1ª reta: '))
lado2 = float(input('Digite o comprimento da 2ª reta: '))
lado3 = float(input('Digite o comprimento da 3ª reta: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')