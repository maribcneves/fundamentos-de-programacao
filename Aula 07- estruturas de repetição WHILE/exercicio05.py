senha = "1"

while senha != '1234':
    senha = input('Digite sua senha: ')

    if senha == '1234':
        print('Acesso permitido.')
    else:
        print('Senha incorreta')