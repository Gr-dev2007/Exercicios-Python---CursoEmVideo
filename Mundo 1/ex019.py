import random
nome1 = str(input('Digite o 1° aluno: '))
nome2 = str(input('Digite o 2° aluno: '))
nome3 = str(input('Digite o 3° aluno: '))
nome4 = str(input('Digite o 4° aluno: '))

lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)
print(f'\n O aluno escolhido foi: {escolha}')
