# Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
# partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
# palavra EMPATE.



time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

quant_gol1 = int(input("Quantos gols o primeiro time fez?"))
quant_gol2 = int(input("Quantos gols o segundo time fez?"))

if quant_gol1 > quant_gol2:
    print(f"O time vencedor foi o {time1}!")
elif quant_gol2 > quant_gol2:
    print(f"O time vencedor foi {time2}!")
else:
    print("Houve empate!")