print('Vamos calcular a soma, a média, o maior e o menor valor de uma lista de números!')

quantidade = int(input('Quantos números você vai informar? '))

soma = 0
maior = float('-inf')
menor = float('inf')

for i in range(1, quantidade + 1):
    numero = float(input(f'Digite o {i}º número: '))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = soma / quantidade

print(f'Soma: {soma}')
print(f'Média: {media:.2f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
