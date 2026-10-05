# Questão 07 

print('Olá! Vamos verificar a situação de matrícula do aluno.')

idade = int(input('Digite a idade do aluno: '))
media = float(input('Digite a média do aluno: '))
frequencia = float(input('Digite o percentual de frequência (ex: 80 para 80%): '))

print('\nTipo de curso:')
print('1 - Graduação')
print('2 - Técnico')
print('3 - Pós-graduação')
tipo_curso = int(input('Escolha o tipo de curso: '))

match tipo_curso:
    case 1:
        if frequencia < 75:
            print('Reprovado por falta.')
        elif media >= 7:
            print('Aprovado.')
        elif media >= 5:
            print('Recuperação.')
        else:
            print('Reprovado.')
    case 2:
        if frequencia < 75:
            print('Reprovado por falta.')
        elif media >= 6:
            print('Aprovado.')
        elif media >= 4:
            print('Recuperação.')
        else:
            print('Reprovado.')
    case 3:
        if frequencia < 75:
            print('Reprovado por falta.')
        elif media >= 7:
            print('Aprovado.')
        else:
            print('Reprovado.')
    case _:
        print('Tipo de curso inválido.')