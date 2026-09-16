# Exercício 03 02/09/26

print('Olá! Escolha dois números e vamos descobrir se são iguais, qual é o maior e o menor entre eles!')

# Perguntas
numero1 = float(input('Digite um número (qualquer um): '))
print('Ótimo!')
numero2 = float(input('Digite outro número (igual ou diferente do anterior): '))

# Operações
igualdade = numero1==numero2
maior_que = numero1>numero2
menor_que = numero1<numero2

# Respostas
print('\nOk! Vamos lá aos resultados.')
print(f'{numero1} == {numero2}? {igualdade}')
print(f'{numero1} > {numero2}? {maior_que}')
print(f'{numero1} < {numero2}? {menor_que}')