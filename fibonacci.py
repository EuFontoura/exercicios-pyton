### crie um programa que retorna a sequência de fibonacci até o número inserido

entrada = int(input("insira um numero inteiro positivo: "))

a, b = 0, 1
sequencia = []

while a <= entrada:
    sequencia.append(a)
    a, b = b, a + b

print(sequencia)