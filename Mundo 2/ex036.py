casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do COMPRADOR? R$'))
anos = int(input('Em quantos anos o COMPRADOR irá pagar?'))

pm = casa / anos
if pm <= salario * 0.3:
    # Código para mensagem verde
    print("\033[32mO EMPRÉSTIMO FOI APROVADO\033[0m")
else:
    # Mensagem vermelha
    print("\033[31mO EMPRÉSTIMO FOI NEGADO\033[0m")