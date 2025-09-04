idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Atleta na categoria: Mirim')
elif idade <= 14:
    print('Atleta na categoria: Infantil')
elif idade <= 19:
    print('Atleta na categoria: Junior')
elif idade <= 20:
    print('Atleta na categoria: Sênior')
else:
    print('Atleta na categoria: Master')