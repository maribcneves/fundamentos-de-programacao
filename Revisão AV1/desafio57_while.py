sexo = input('Digite seu sexo. Use M para masculino e F para feminino: ')

while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
    print('Ops! Dado incorreto, responda novamente.')
    sexo = input('Digite seu sexo. Use M para masculino e F para feminino: ')

if sexo == 'M' or sexo == 'm':
    print('Entendi, sexo masculino.')
else:
    print('Entendi, sexo feminino.')