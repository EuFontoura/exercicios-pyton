# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioAntigo = float(input("Insira seu salário atual: "))
percentualAumento = 0


if salarioAntigo <= 280:
    percentualAumento = 20
    salarioNovo = salarioAntigo + (salarioAntigo * 0.2)
elif 281 < salarioAntigo < 700:
    percentualAumento = 15
    salarioNovo = salarioAntigo + (salarioAntigo * 0.15)
elif 700 < salarioAntigo < 1500:
    percentualAumento = 10
    salarioNovo = salarioAntigo + (salarioAntigo * 0.1)
else:
    percentualAumento = 5
    salarioNovo = salarioAntigo + (salarioAntigo * 0.05)

valorAumento = salarioNovo - salarioAntigo

print(f"Salário anterior: R${salarioAntigo:.2f}")
print(f"Novo salário: R${salarioNovo:.2f}")
print(f"Percentual aplicado: {percentualAumento}%")
print(f"Valor do aumento: R${valorAumento:.2f}")
