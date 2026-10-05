usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while usuario != 'admin' or senha != '1234':
    print('Dados incorretos. Preencha novamente.')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

    if usuario == 'admin' and senha == '1234':
        print('Acesso permitido.')