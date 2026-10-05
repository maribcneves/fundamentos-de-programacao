print('Olá! Faça o calculo do preço da sua passagem conosco!')

distancia = int(input('Qual será a distância a ser percorrida? '))
preco_1 = distancia * 0.50
preco_2 = distancia * 0.45

if distancia <= 200:
    print('Entendi! O preço da sua passagem é ')