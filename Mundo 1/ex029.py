velocidade = float(input('Digite a velocidade do carro em Km/h: '))
limite = 80
if velocidade <= limite:
    print('Tenha um bom dia! Dirija com segurança')
else:
    multa = (velocidade - limite) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \n Você deve pagar uma multa de R${:.2f}'.format(multa))
