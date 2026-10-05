print('Olá! Escolha 3 números diferentes entre si e vou te dizer qual é o maior e o menor entre eles!')

num_1 = int(input('Digite o 1º número: '))
num_2 = int(input('Digite o 2º número: '))
num_3 = int(input('Digite o 3º número: '))

#BLOCO MAIOR NÚMERO
if num_1 >= num_2 and num_1 >= num_3:
    print(f'O número {num_1} é o maior.')

elif num_2 >= num_1 and num_2 >= num_3:
    print(f'O número {num_2} é o maior.')

else:
    print(f'O número {num_3} é o maior.')

#BLOCO MENOR NÚMERO
if num_1 <= num_2 and num_1 <= num_3:
    print(f'O número {num_1} é o menor.')

elif num_2 <= num_1 and num_2 <= num_3:
    print(f'O número {num_2} é o menor.')

else:
    print(f'O número {num_3} é o menor.')