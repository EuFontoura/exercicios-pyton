### Crie um programa ondeo usuário insere um número e é retornada a tabuada referente ao mesmo

entrada = int(input("insira um numero inteiro positivo: "))

for i in range(1, 11):
    print(f"{entrada} x {i} = {entrada * i}")
