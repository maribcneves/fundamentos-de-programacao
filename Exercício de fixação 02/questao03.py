print('Vamos calcular a soma de 1 até o número que você escolher!')

n = int(input('Digite um número inteiro positivo: '))

soma = 0
for i in range(1, n + 1):
    soma += i

print(f'Soma = {soma}')
