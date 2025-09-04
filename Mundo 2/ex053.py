# Programa para verificar palíndromos

frase = input("Digite uma frase: ")

# Remover espaços e deixar tudo em minúsculas
frase_formatada = frase.replace(" ", "").lower()

# Verificar se a frase é igual à sua inversa
if frase_formatada == frase_formatada[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
