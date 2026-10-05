print('===== CAIXA ELETRÔNICO =====')

saldo = 1000.00
opcao = 0

while opcao != 4:
    print('\n1 - Consultar saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')
    opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:
        print(f'\nSaldo atual: R${saldo:.2f}')
    elif opcao == 2:
        valor = float(input('Digite o valor do depósito: R$'))
        saldo += valor
        print('\nDepósito realizado com sucesso!')
        print(f'Saldo atual: R${saldo:.2f}')
    elif opcao == 3:
        valor = float(input('Digite o valor do saque: R$'))
        if valor > saldo:
            print('\nSaldo insuficiente para realizar o saque.')
        else:
            saldo -= valor
            print('\nSaque realizado com sucesso!')
            print(f'Saldo atual: R${saldo:.2f}')
    elif opcao == 4:
        print('\nObrigado por utilizar o caixa eletrônico. Até logo!')
    else:
        print('\nOpção inválida.')
