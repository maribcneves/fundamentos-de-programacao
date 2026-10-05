# Exercício 01 sala 09/09/26

print('Olá! Este programa serve para verificar se o seu aluno está aprovado ou reprovado em matemática neste ano. Siga com os preenchimentos abaixo para saber o resultado final do aluno.')

# Perguntas
nome = input('Digite o nome do aluno: ')
nota_av1 = float(input('Digite a nota da AV1: '))
nota_av2 = float(input('Digite a nota da AV2: '))
nota_av3 = float(input('Digite a nota da AV3: '))
print('Ok! Agora vou calcular.')

# Operação
media_aluno = float((nota_av1 + nota_av2 + nota_av3)/ 3)

# Resposta condicional
if media_aluno >= 7:
    print(f'Aprovado! A média de {nome} é {media_aluno: .2f}!')
else:
    print(f'Reprovado! A média de {nome} é {media_aluno: .2f}!')