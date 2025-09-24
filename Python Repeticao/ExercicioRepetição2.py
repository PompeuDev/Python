## Dados o numero n de alunos de uma turma de Algoritmos e suas notas da primeira prova determinar a media das notas

alunos = int(input("Digite o numero de alunos: "))

soma = 0
contador = 1
contador_bomaluno = 0
contador_malaluno = 0

while contador <= alunos:
    nota = float(input("Digite as notas da primeira prova: "))
    soma += nota
    contador += 1

    if nota >= 5.0:
        contador_bomaluno += 1
    elif nota < 5.0:
        contador_malaluno +=1   

media = soma / alunos



print(f"A media das notas é {media:.2f} e houveram {contador_bomaluno} notas acima de 5.0 e {contador_malaluno} abaixo de 5.0!")
