soma = 0
quantidade = 0

while True:
    numero = float(input('Digite um número: '))
    soma += numero
    quantidade += 1

    continuar = input('Você deseja continuar? Digite S ou N: ')
    if continuar != 'S':
        break

media = soma / quantidade

print(f'A soma dos números deu {soma}, e a média deu {media:.2f}.')