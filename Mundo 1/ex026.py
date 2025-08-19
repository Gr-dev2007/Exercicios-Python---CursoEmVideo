frase = str(input('Digite uma frase: ')).strip().upper()

print('Na sua frase a letra "A" aparece {} vezes '.format(frase.count('A')))
print('A primeira vez que a letra "A" é na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" aparece é na posição {}'.format(frase.rfind('A')+1))
