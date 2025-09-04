soma = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print(f'\nA soma entre os números ímpares e múltiplos de 3 é: {soma}')

