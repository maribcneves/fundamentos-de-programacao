print('Vamos mostrar os números pares de 1 até o número que você escolher!')

n = int(input('Digite um número inteiro positivo: '))

quantidade = 0

print('Números pares:')
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        quantidade += 1

print(f'Quantidade de números pares: {quantidade}')
