# Questão 03 - Elegibilidade para bolsa

print('Olá! Vamos verificar se o aluno pode receber uma bolsa.')

# Perguntas
media = float(input('Digite a média acadêmica: '))
freq = float(input('Digite o percentual da frequência: '))
renda = float(input('Digite a renda familiar: '))
se_bolsa = input('O aluno já tem bolsa? Digite S ou N: ')

# Lógica

media_ok = media >= 7
freq_ok = freq >= 75
renda_ok = renda <= 3000
bolsa_ok = se_bolsa == 'N' or 'n'

# Resposta
if media_ok and freq_ok and renda_ok and bolsa_ok:
    print('O aluno cumpre os requisitos e está elegível para a bolsa!')
else:
    print('Poxa, o aluno não está elegível pelos motivos a seguir:')
    if not media_ok:
        print('- Média insuficiente.')
    if not freq_ok:
        print('- Frequência insuficiente.')
    if not renda_ok:
        print('- Renda acima do limite.')
    if not bolsa_ok:
        print('- Já possui outra bolsa.')    