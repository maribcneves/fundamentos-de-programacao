soma = 0

while True:
    numero = int(input('Digite um número (e 0 para parar): '))
    soma += numero

    if numero == 0:
        break

print(f'A soma total dos números foi igual a {soma}.')