# Exercício 3 - Introdução à Programação 26/08/26

# Frase de abertura
print('Olá! Vamos às compras. Hoje você tem 3 produtos para escolher. Simule aqui o valor total da feira antes de ir ao mercado!')

# Perguntasinput(
produto_one = input('\nDigite o nome do 1º produto: ')
valor_one = float(input(f'Quanto custa o {produto_one}? '))
quantidade_one = int(input(f'Qual é a quantidade de {produto_one} que você precisa? '))
produto_two = input('Digite o nome do 2º produto: ')
valor_two = float(input(f'Quanto custa o {produto_two}? '))
quantidade_two = int(input(f'Qual é a quantidade de {produto_two} que você precisa? '))
produto_three = input('Digite o nome do 3º produto: ')
valor_three = float(input(f'Quanto custa o {produto_three}? '))
quantidade_three = int(input(f'Qual é a quantidade de {produto_three} que você precisa? '))

# Operações
custo_one = float(valor_one*quantidade_one)
custo_two = float(valor_two*quantidade_two)
custo_three = float(valor_three*quantidade_three)
custo_total = float(custo_one+custo_two+custo_three)

# Resposta
print('\nEntendi! Aqui está o resumo da simulação da sua compra: ')
print(f'{produto_one}: {quantidade_one} x R${valor_one} = R${custo_one:.2f}.')
print(f'{produto_two}: {quantidade_two} x R${valor_two} = R${custo_two:.2f}.')
print(f'{produto_three}: {quantidade_three} x R${valor_three} = R${custo_three:.2f}.')
print(f'TOTAL GERAL: R${custo_total}.')
print('\nBoas compras!')