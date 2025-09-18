# Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de
# Computational Thinking, o número de aulas ministradas e o número de aulas assistidas por
# este aluno nesta disciplina. Calcule e mostre a média final deste aluno e diga se ele foi
# aprovado ou reprovado ou está de exame. Lembrando que a média do primeiro semestre tem
# peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentado mais de 70% das
# aulas.

n1 = float(input("Digite a media do seu primeiro semestre: "))
n2 = float(input("Digite a media do seu segundo semestre: "))
num_aula = int(input("Digite a quantidade de aulas que foram ministradas: "))
num_freq = int(input("Digite quantas aulas você foi nesse semestre: "))

media = (n1*4 + n2*6)/10
freq_aluno = num_freq/num_aula

if media >= 6.0 and freq_aluno >= 0.7:
    print("VOCÊ FOI APROVADO!")
else:
    print("VOCÊ FOI REPROVADO!")

