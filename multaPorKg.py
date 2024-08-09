### João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = int(input("Insira o peso do peixe: "))
pesoMax = int(50)
excesso = 0
valorMulta = 4

if pesoPeixe > pesoMax:
    excesso = pesoPeixe - pesoMax
    multa = float(excesso * valorMulta)
    print(f"O peso do peixe excedeu {excesso}kg, o valor da multa a ser pago será de R${multa:.2f}")
else:
    print(f"Peso do peixe não excede ao peso máximo")

