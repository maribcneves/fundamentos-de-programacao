print('Vamos descobrir se o ano é bissexto ou não.')

ano = int(input('Digite o ano que você deseja saber se é bissexto ou não: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')

else:
    print(f'O ano {ano} não é bissexto!')