# Uma equação de 2º grau é da forma: ax2 + bx + c = 0, onde a ̸= 0. Escreva um algoritmo
# que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível.
# Use a seguinte fórmula para resolver a equação:

# delta = #b2 - 4ac
# raiz1 = -b + raiz quadrada de delta / 2a
# raiz2 = -b - raiz quadrada de delta /2a
# a diferente de 0
import math
a = int(input("Digite o A: "))
b = int(input("Digite o B: "))
c = int(input("Digite o C: "))

if a == 0:
    print("Nao é possivel realizar a equação.")

else:
    delta = b**2 - 4*a*c  # cálculo do discriminante

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: {x1:.2f} e {x2:.2f}")
