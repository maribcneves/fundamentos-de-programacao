print('Vamos calcular o seu aumento salarial deste semestre!')

salario = float(input('Digite o seu salário atual: '))
aumento_1 = (salario * 0.10)
salario_final_1 = (salario * 1.10)

aumento_2 = (salario * 0.15)
salario_final_2 = (salario * 1.15)

if salario <= 1250:
    print(f'Seu aumento será de R$ {aumento_2}.\nLogo, seu novo salário será de R$ {salario_final_2: .2f}.')

else:
    print(f'Seu aumento será de R$ {aumento_1}.\nLogo, seu novo salário será de R$ {salario_final_1: .2f}.')