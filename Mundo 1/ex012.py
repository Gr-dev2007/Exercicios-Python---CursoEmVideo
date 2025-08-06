valor = float(input('Digite o valor do produto: R$'))

des = valor * 0.05
vades = valor - des
print (f'O desconto desse produto é de R${des:.2f} e o valor final é de R${vades:.2f}')