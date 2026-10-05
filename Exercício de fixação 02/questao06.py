print('Vamos validar a sua senha!')

senha_correta = 1234

senha = int(input('Digite a senha: '))

while senha != senha_correta:
    print('Senha incorreta, tente novamente.')
    senha = int(input('Digite a senha: '))

print('Acesso autorizado!')
