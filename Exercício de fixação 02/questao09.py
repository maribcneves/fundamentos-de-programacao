print('Vamos descobrir o maior e o menor número de uma lista, e a diferença entre eles!')

quantidade = int(input('Quantidade de números: '))

maior = float('-inf')
menor = float('inf')

for i in range(1, quantidade + 1):
    numero = int(input(f'Digite o {i}º número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

diferenca = maior - menor

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Diferença: {diferenca}')
