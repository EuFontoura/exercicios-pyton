### Crie um programa que retorna o fatorial de um número inserido

number = int(input("insira um número inteiro: "))

fatorial = 1

if number < 0:
    print("o numero escolhido não é um número inteiro")
else:
    for i in range(1, number+1):
        fatorial *= i

    print(f"o fatorial de {number} é {fatorial}")