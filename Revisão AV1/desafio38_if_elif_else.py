num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))

if num1 > num2:
    print(f'O número 1 ({num1}) é maior que o número 2 ({num2}).')

elif num2 > num1:
    print(f'O número 2 ({num2}) é maior que o número 1 ({num1}).')

else:
    print('Os dois números são iguais!')