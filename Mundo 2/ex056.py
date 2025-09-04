idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menor_20 = 0

for c in range(0, 4):
    nome = input(f'Digite o nome da {c + 1}ª pessoa: ')
    idade = int(input(f'Digite a idade da {c + 1}ª pessoa: '))
    total_idade += idade

    # Seleção de sexo com validação
    while True:
        sexo = input(f'Selecione o sexo da {c + 1}ª pessoa (M/F): ').strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Opção inválida! Digite apenas M ou F.")

    # Homem mais velho
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    # Mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

media_idade = total_idade / 4

print(f'\nA média de idade do grupo é {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'O nome do homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Número de mulheres com menos de 20 anos: {mulheres_menor_20}')
