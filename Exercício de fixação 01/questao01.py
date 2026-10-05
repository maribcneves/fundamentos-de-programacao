# Questão 01 - Classificação de idade

print('Olá! Vamos descobrir, de acordo com sua idade, de qual grupo você faz parte.')

# Pergunta
idade = int(input('Digite sua idade: '))

# Resposta
if idade >= 0 and idade < 13:
    print(f'Você tem {idade} anos. Logo, é uma criança.')
elif idade >= 13 and idade < 18:
    print(f'Você tem {idade} anos. Logo, é um adolescente.')
elif idade >= 18 and idade < 60:
    print(f'Você tem {idade} anos. Logo, é um adulto.')
elif idade >= 60:
    print(f'Você tem {idade}. Logo, é idoso.')
else:
    print(f'Ops! {idade} anos é uma idade inválida. Digite um número maior que 0.')