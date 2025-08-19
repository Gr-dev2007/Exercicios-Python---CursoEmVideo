salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    aumento = salario * 0.10  # 10% de aumento
else:
    aumento = salario * 0.15  # 15% de aumento

novo_salario = salario + aumento
print(f'O seu novo salário será R${novo_salario:.2f}')