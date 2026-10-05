print('Este aplicativo serve para você simular se o seu empréstimo para comprar uma casa seria aprovado.')

valor = float(input('Digite o valor da casa que você quer comprar: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos você quer concluir o pagamento: '))

meses = anos * 12

prestacao_mensal = valor / meses
limite = 0.30 * salario

if prestacao_mensal < limite:
    print(f'Empréstimo aprovado! O valor da prestação mensal será R${prestacao_mensal: .2f}.')

elif prestacao_mensal == limite:
    print(f'Empréstimo aprovado! O valor da prestação mensal será R${prestacao_mensal: .2f}.')

else:
    print('O empréstimo será negado!')