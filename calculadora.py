### Crie uma calculadora simples

number1 = input("Digite o primeiro numero: ")
number2 = input("Digite o segundo numero: ")
operacao = input("escolha uma operação (+, -, *, /):")

if operacao == '+':
    resultado = number1 + number2
elif operacao == '-':
    resultado = number1 - number2
elif operacao == '*':
    resultado = number1 * number2
elif operacao == '/':
    if number2 != 0:
        resultado = number1 / number2
    else: print("Erro, divisão por zero")
else:
    print('por favor, escolha uma das opções acima')

print(f"Resultado: {resultado}")