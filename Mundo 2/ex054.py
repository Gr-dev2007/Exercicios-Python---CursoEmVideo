from datetime import date

anoatual = date.today().year
maiores = 0
menores = 0

for c in range(0, 7):
    nascimento = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    idade = anoatual - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Das \033[33m7 pessoas\033[0m, '
      f'\033[32m{maiores}\033[0m já são maiores de idade'
      f' e \033[31m{menores}\033[0m ainda não atingiram a maioridade.')
