from datetime import date

ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print('Você ainda vai se alistar')
    print('Falta {} anos'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou do tempo de se alistar')
    print('Já se passou {} anos'.format(idade - 18))