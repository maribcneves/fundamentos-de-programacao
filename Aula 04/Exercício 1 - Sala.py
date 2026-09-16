# Exercício 01 02/09/26

print('Olá! Vamos treinar as operações matemáticas. Escolha 2 números e veja o resultado das principais operações!')

# Perguntas
numero1 = float(input('Digite um número (qualquer um): '))
print('Ótimo!')
numero2 = float(input('Digite outro número (igual ou diferente do anterior): '))

# Operações
soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

# Respostas
print('\nOk! Vamos lá aos resultados.')
print(f'{numero1} + {numero2} = {soma}')
print(f'{numero1} - {numero2} = {subtracao}')
print(f'{numero1} * {numero2} = {multiplicacao}')
print(f'{numero1} / {numero2} = {divisao: .2f}')