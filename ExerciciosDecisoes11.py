# Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler
# 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido.
# Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

dia = int(input("Escreva o DIA no formato DD: "))
mes = int(input("Escreva o MES no formato MM: "))

if dia > 0 and dia <= 31:
    if mes > 0 and mes < 12: 
        print("Você deu uma data valida!")
else:
    print("A data é invalida!")
