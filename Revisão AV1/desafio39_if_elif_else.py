print('Olá! Esta é a calculadora do alistamento militar. Responda os campos abaixo.')

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2026

idade = ano_atual - ano_nascimento

tempo_faltante = 18 - idade
tempo_passado = idade - 18

if idade < 18:
    print(f'Você tem {idade} anos, e só vai precisar se alistar daqui a {tempo_faltante} anos.')

elif idade == 18:
    print(f'Você tem {idade} anos. Já está na hora de se alistar!')

else:
    print(f'Você tem {idade} anos, e já passou {tempo_passado} anos do seu tempo de alistamento')