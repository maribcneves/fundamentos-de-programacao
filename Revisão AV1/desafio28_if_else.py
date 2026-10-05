print('Vamos jogar! Vou pensar em um número inteiro entre 0 e 5 e você vai tentar chutar o número que eu pensei.')

numero = int(input('Digite um número inteiro entre 0 e 5: '))

if numero == 4:
    print(f'Isso mesmo, que sorte! Pensei no número {numero}.\nVOCÊ VENCEU!')

else:
    print(f'Ihhh, errou! Eu pensei no número 4.\nVOCÊ PERDEU!')