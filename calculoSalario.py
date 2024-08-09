# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valorHora = float(input("Insira o valor da sua hora de trabalho: "))
horasTrabalhadas = float(input("Insira a quantidade de horas trabalhadas no mês: "))

SalarioBruto = valorHora * horasTrabalhadas
porcentagemImpostoRenda = 0
porcentagemSindicato = 0.03
porcentagemFGTS = 0.11

if SalarioBruto <= 900:
    impostoRenda = 0
elif  900 < SalarioBruto <= 1500:
    porcentagemImpostoRenda = 5
    impostoRenda = SalarioBruto * 0.05
elif  1500 < SalarioBruto <= 2500:
    porcentagemImpostoRenda = 10
    impostoRenda = SalarioBruto  * 0.10
else:
    porcentagemImpostoRenda = 20
    impostoRenda = SalarioBruto * 0.20

valorFGTS = SalarioBruto * porcentagemFGTS
descontoSindicato = SalarioBruto * porcentagemSindicato
totalDescontos = impostoRenda + descontoSindicato
SalarioLiquido = SalarioBruto - totalDescontos

print(f"Salário Bruto: R${SalarioBruto:.2f}")
print(f"(-) IR ({porcentagemImpostoRenda}%): R${impostoRenda:.2f}")
print(f"(-) Sindicato (3%): R${descontoSindicato:.2f}")
print(f"FGTS (11%): R${valorFGTS:.2f} ")
print(f"Total de descontos: R${totalDescontos:.2f}")
print(f"Salário líquido: R${SalarioLiquido:.2f}")
