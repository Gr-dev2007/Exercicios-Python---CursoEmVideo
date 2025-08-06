from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo em graus: '))

rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O ângulo de {angulo}° tem:')
print(f' - Seno: {seno:.2f}')
print(f' - Cosseno: {cosseno:.2f}')
print(f' - Tangente: {tangente:.2f}')
