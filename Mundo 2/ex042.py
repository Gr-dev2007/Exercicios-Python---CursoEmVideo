reta1 = int(input('Digite o primeiro valor: '))
reta2 = int(input('Digite o segundo valor: '))
reta3 = int(input('Digite o terceiro valor: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos podem formar um triângulo')

    if reta1 == reta2 == reta3:
        print('Tipo: EQUILÁTERO (todos os lados iguais)')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Tipo: ISÓSCELES (dois lados iguais)')
    else:
        print('Tipo: ESCALENO (todos os lados diferentes)')
else:
    print('Os segmentos NÃO podem formar um triângulo')
