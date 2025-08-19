import random
num = int(input('Advinhe um número entre 0 e 5: '))

escolha = random.choice([0, 1, 2, 3, 4, 5])
if num == escolha:
    print('Vc acertou!')
else:
    print('Vc errou! Eu pensei no número {}'.format(escolha))

