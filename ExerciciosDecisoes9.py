# Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
# seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

# 1 - A vista em dinheiro ou cheque, recebe 10% de desconto
# 2 - A vista no cartão de crédito, recebe 5% de desconto
# 3 - Em duas vezes, preço normal de etiqueta sem juros
# 4 - Em quatro vezes, preço normal de etiqueta mais juros de 7%

preco = float(input("Digite o preço do produto: "))
print("\nEscolha a forma de pagamento:")
print("1 - À vista em dinheiro ou cheque (10% de desconto)")
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Em duas vezes (sem juros)")
print("4 - Em quatro vezes (7% de juros)")

opcao = int(input("Digite a opção escolhida (1-4): "))


if opcao  == 1:
    valor_final = preco * 0.90
    print (f"O desconto será de 10% e você pagará R${valor_final} reais")
elif opcao == 2:
    valor_final = preco * 0.95
    print (f"O desconto será de 5% e você pagará R${valor_final} reais")
elif opcao == 3:
    valor_final = preco
    print (f"Será cobrado o valor da etiqueta e você pagará R${valor_final} reais")
elif opcao == 4:
    valor_final = preco * 1.07
    parcela = valor_final/4
    print (f"O parcelamento em 4 vezes é cobrado 7% de juros e você pagará R${valor_final:.2f} reais e sua parcela será de R${parcela:.2f} reais.")


