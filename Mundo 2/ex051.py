primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(10):  # repete 10 vezes
    termo = primeiro + i * razao
    print(termo, end=' ')
