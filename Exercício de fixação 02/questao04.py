print('Vamos mostrar a tabuada do número que você escolher!')

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
