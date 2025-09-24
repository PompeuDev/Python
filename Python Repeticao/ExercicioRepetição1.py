## Dada uma sequencia de numeros inteiros onde o ultimo elemento é o 0,escreva um algoritmo que calcula a soma dos numeros pares de sequencia.


soma = 0

numero = int(input("Digite um numero: "))

while numero != 0:
    if numero % 2 == 0:
        soma += numero
        numero = int(input("Digite um numero: "))

print("A soma dos numeros pares é: ", soma)