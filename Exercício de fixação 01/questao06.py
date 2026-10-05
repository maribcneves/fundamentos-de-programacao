# Questão 06 

print('1 - Cadastrar aluno')
print('2 - Consultar aluno')
print('3 - Alterar aluno')
print('4 - Excluir aluno')
print('5 - Listar alunos')
print('6 - Sair')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        print('Cadastrar aluno')
    case 2:
        print('Consultar aluno')
    case 3:
        print('Alterar aluno')
    case 4:
        print('Excluir aluno')
    case 5:
        print('Listar alunos')
    case 6:
        print('Saindo...')
    case _:
        print('Opção inválida.')