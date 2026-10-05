print('Vamos digitar 10 números e calcular algumas estatísticas!')

numero = int(input('Digite o 1º número: '))

soma = numero
maior = numero
menor = numero

if numero % 2 == 0:
    pares = 1
    impares = 0
else:
    pares = 0
    impares = 1

contador = 2

while contador <= 10:
    numero = int(input(f'Digite o {contador}º número: '))

    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print(f'Soma total: {soma}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Quantidade de pares: {pares}')
print(f'Quantidade de ímpares: {impares}')