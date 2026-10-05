# Questão 05 - Classificação de desempenho

print('Olá! Vamos classificar o desempenho do funcionário.')

produtividade = float(input('Digite a nota de produtividade: '))
qualidade = float(input('Digite a nota de qualidade: '))
presenca = float(input('Digite o percentual de presença (ex: 80 para 80%): '))

media = (produtividade + qualidade) / 2

if presenca < 75:
    print('Desempenho comprometido por baixa frequência.')
elif media >= 9 and presenca >= 90:
    print('Excelente.')
elif media >= 7 and presenca >= 85:
    print('Bom.')
elif media >= 5 and presenca >= 75:
    print('Regular.')
else:
    print('Insatisfatório.')