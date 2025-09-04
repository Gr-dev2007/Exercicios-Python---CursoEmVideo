# Programa de conversão de números

num = int(input("Digite um número inteiro: "))
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} em octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} em hexadecimal é {hex(num)[2:].upper()}")
else:
    print("Opção inválida!")
