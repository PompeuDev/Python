# A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
# trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
# da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
# apenas nos dias úteis, escreva um algoritmo que recebe:
# a) o total de dias úteis de um mês
# b) o total de horas trabalhadas pelo trabalhador
# c) quanto o trabalhador recebe por hora
# Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do
# trabalhador.








dias_uteis = int(input("Quantos dias uteis você trabalha por mês?"))
horas_trab =int(input("Quantas horas voce trabalha no mês"))
valor_hora = float(input("Quanto você recebe por hora?"))
hora_extra = 0

jornada_mensal = dias_uteis * 8
salario_conv = jornada_mensal * valor_hora

if horas_trab > jornada_mensal:
    hora_extra = horas_trab - jornada_mensal
    print(f"Você fez {hora_extra} horas extras esse mês")
else: 
    print("Você nao fez horas extras esse mês")

valor_extra = valor_hora + (0.5*valor_hora)
valor_exc = valor_extra * hora_extra

        
print (f"Você tem R${valor_exc} a receber")

salario_final = valor_exc + salario_conv

print(f"O seu valor de salario final ficou de {salario_final} reais")