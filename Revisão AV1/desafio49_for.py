print('Olá! Escolha um número e vamos te mostrar a tabuada dele.')

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

print(f'Fim da tabuada do número {numero}.')