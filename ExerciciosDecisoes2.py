#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
# houve um empate.



n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"O primeiro numero é maior que o segundo numero")
elif n2 > n1:
    print(f"O segundo numero é maior que o primeiro numero")
elif n1 == n2:
    print("Os numeros são iguais!")
