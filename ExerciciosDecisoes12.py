# Agora, vamos acrescentar na verificação de data os casos de ano bissexto, ou seja, o ano que
# fevereiro tem 29 dias. Um ano é bissexto se:
# a) o ano for divisível por 4
# b) anos múltiplos de 100, não são bissextos
# c) quando o ano for divisível por 400 ele é bissexto
# d) as últimas regras prevalecem sobre as primeiras
# Para exemplificar um pouco essas regras, observe que 1900 não foi bissexto mas 2000 foi.

ano = int(input("Digite o ano no formato AAAA: "))

if ano % 4 == 0:
    print("O ano é Bissexto!")
elif ano % 400 == 0:
    print("O ano é Bissexto!")
elif ano % 100 == 0:
    print("O ano nao é bissexto!")
else:
    print("O ano nao é bissexto!")