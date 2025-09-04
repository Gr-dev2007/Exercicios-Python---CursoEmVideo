maior = 0
menor = 0

for c in range (0,5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa: '))

    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso digitado foi: {maior}kg.')
print(f'O menor peso digitado foi: {menor}kg.')