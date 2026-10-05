# Exercício 03 sala 09/09/26

print('Este programa vai te dizer se você é maior ou menor de idade no Brasil.')

# Pergunta
idade = int(input('Quantos anos você tem? (use este formato: 18) '))

# Resposta
if idade > 18:
    print(f'\nEntendi! A maior idade no Brasil é 18 anos. Você tem {idade} anos, logo você é maior de idade.')
else:
    print(f'\nEntendi! A maior idade no Brasil é 18 anos. Você tem {idade} anos, logo você é menor de idade.')