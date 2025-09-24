## Escreva um algoritmo que, dados um numero inteiro positivo N, imprime na tela a contagem de todos os divisiroes positivos de N       
numero = int(input("Digite um numero: "))
conta_divisores = 1

while conta_divisores <= numero:
    if numero % conta_divisores == 0:
        print(conta_divisores)
    conta_divisores += 1

