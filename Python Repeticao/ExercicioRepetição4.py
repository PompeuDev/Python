## Dados N um inteiro positivo e uma sequencia de N numeros reais, escrava um algoritmo que conta e imprime a quantidade de numeros positivos e a quantidades de numeros negativos.
limite = int(input("Digite a quantidade de numeros que quer digitar: "))
contador_positivo = 0
contador_negativo = 0
controle = 0

while limite > controle:
    numero = float(input("Digite um numero: "))
    if numero % 2 == 0:
        contador_positivo += 1
    elif numero % 2 != 0:
        contador_negativo += 1
    controle += 1

print(f"Existem {contador_positivo} numeros positivos e {contador_negativo} numeros negativos!")

