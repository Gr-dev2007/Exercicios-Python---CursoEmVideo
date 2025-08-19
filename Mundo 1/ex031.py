dis = float(input('Digite a distância da sua viagem em KM: '))
preco = dis * 0.50
preco2 = dis * 0.45
if dis <= 200:
    print('O valor da sua passa é: R${:.2f}'.format(preco))
else:
    print('O valor da sua passagem é: R${:.2f}'.format(preco2))