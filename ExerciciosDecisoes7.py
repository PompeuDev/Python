# Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
# tabela a seguir:
# Categoria Idade
# Infantil 5 a 7
# Juvenil 8 a 10
# Adolescente 11 a 15
# Adulto 16 a 30
# Senior acima de 30

idade = int(input("Digite a sua idade: "))

if idade < 7:
    print("Você é da categoria Infantil!")
elif idade < 10:
    print("Você é da categoria Juvenil!")
elif idade < 15:
    print("Você é da categoria Adolescente!")
elif idade < 30:
    print("Você é da categoria Adulto!")
else:
    print("Você já é um Senior!")