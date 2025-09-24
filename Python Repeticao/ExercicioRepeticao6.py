nota = int(input("Nota do alno:  "))
maior = nota
menor = nota
contador = 1


while contador < 20:
    nota = int(input("Nota do aluno:  "))
    if nota > maior:
    maior = nota
    if nota < menor:
    menor = nota
    contador += 1    