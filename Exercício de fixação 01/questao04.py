# Questão 04 - Sistema de empréstimo

print('Olá! Vamos começar a sua análise de solicitação de empréstimo.')

# Pergunta
idade = int(input('Digite a sua idade: '))
salario = float(input('Digite seu salário: '))
tempo = int(input('Digite há quanto tempo você trabalha em meses: '))
valor = float(input('Digite o valor de empréstimo que você deseja: '))

# Resposta
if idade < 18:
    print('Empréstimo não permitido.')
elif salario < 1500:
    print('Renda insuficiente.')
elif tempo < 12:
    print('Tempo de trabalho insuficiente.')
elif valor > 10 * salario:
    print('Valor solicitado muito alto.')
else:
    print('Empréstimo pré-aprovado!')