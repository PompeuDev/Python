# Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

A = int(input("Digite um valor inteiro: "))
B = int(input("Digite outro valor inteiro: "))

if A % B == 0:
    print("O primeiro numero é divisivel pelo segundo!")
else:  
    print("Os numeros nao são divisiveis!")