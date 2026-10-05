# Questão 02 - Classificação de produto

print('Olá, vamos classificar os produtos de acordo com o preço e a quantidade disponível.')

# Pergunta
preco_prod = float(input('Digite o valor em reais do produto (maior ou igual a 0): '))
qtd_estoque = int(input('Digite a quantidade do produto que tem em estoque (maior que 0): '))

# Enquanto o preço ou a quantidade for inválido, o sistema pede de novo
while preco_prod <= 0 or qtd_estoque < 0:
    print('\nOps! Preço ou quantidade inválidos. Preencha novamente.')
    preco_prod = float(input('Digite o valor em reais do produto (maior ou igual a 0): '))
    qtd_estoque = int(input('Digite a quantidade do produto que tem em estoque (maior que 0): '))

print('\nVamos à análise abaixo: ')

# Resposta
if preco_prod > 1000 and qtd_estoque < 5:
    print(f'Produto caro com estoque crítico.\n- R${preco_prod: .2f};\n{qtd_estoque} em estoque.')
elif preco_prod > 1000 and 5 <= qtd_estoque <= 20:
    print(f'Produto caro com estoque normal.\n- R${preco_prod: .2f};\n{qtd_estoque} em estoque.')
elif preco_prod > 1000 and qtd_estoque > 20:
    print(f'Produto caro com estoque alto.\n- R${preco_prod: .2f};\n{qtd_estoque} em estoque.')
elif  preco_prod <= 1000 and qtd_estoque < 5:
    print(f'Estoque crítico!\n- R${preco_prod: .2f};\n- {qtd_estoque} em estoque.')
else:
    print('Estoque normal!')