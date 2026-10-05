print('Vamos contar quantos números positivos, negativos e iguais a zero você digitar!')

positivos = 0
negativos = 0
zeros = 0

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número: '))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

print(f'Quantidade de positivos: {positivos}')
print(f'Quantidade de negativos: {negativos}')
print(f'Quantidade de zeros: {zeros}')
