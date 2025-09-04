num = int(input("Digite um número: "))

if num > 1: #números menores que dois não são primos
    for i in range(2, int(num ** 0.5) + 1): #é mais eficiente testar divisores até a raiz quadrada do número.
        if num % i == 0: #Se algum divisor divide exatamente (num % i == 0), não é primo
            print(f"{num} não é primo")
            break
    else:
        print(f"{num} é primo")
else:
    print(f"{num} não é primo") #números menores que dois não são primos
