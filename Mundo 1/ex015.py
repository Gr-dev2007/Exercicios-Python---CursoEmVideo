km = float(input('Quantos KM foram percorridos? '))
dia = float(input('Quantos dias alugados? '))
aluguel = (km * 0.15) + (dia * 60)
print(f'O valor do aluguel é de R${aluguel:.2f}')