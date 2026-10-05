print('Esta calculadora serve para você ver se foi multado(a) por excesso de velocidade e caso sim, qual é o valor da multa.')

velocidade = int(input('Digite a velocidade em km/hr do carro: '))
multa = 7 * (velocidade - 80)

if velocidade > 80:
    print(f'Você estava acima do limite permitido. Sua multa vai ser de R$ {multa}.')

else:
    print('Você estava dentro do limite de velocidade e não vai levar multa!')