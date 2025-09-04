preco = float(input('Qual é o preço do produto? R$'))

print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] Em até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')

opcao = int(input('Escolha a opção de pagamento: '))

if opcao == 1:
    total = preco - (preco * 0.10)
    print(f'O valor final com 10% de desconto será R${total:.2f}')
elif opcao == 2:
    total = preco - (preco * 0.05)
    print(f'O valor final com 5% de desconto será R${total:.2f}')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'O valor final será R${total:.2f}, em 2x de R${parcela:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 0.20)
    parcela = total / parcelas
    print(f'O valor final será R${total:.2f}, em {parcelas}x de R${parcela:.2f} (com juros)')
else:
    total = preco
    print('Opção inválida! Tente novamente.')
