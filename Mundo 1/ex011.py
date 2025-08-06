largura = float(input('Qual a largura da sua parede (em metros)? '))
altura = float(input('Qual a altura da sua parede (em metros)? '))
area = largura * altura
tinta = area / 2
print(f'\n A área da sua parede equivale à {area}m \n Serão necessários {tinta:.0f} latas de tinta para pintar a parede completa')