### Crie um programa que determina se uma frase é um palíndromo ou não ###

entrada = input("Insira uma palavra ou frase: ")

# aqui nós iteramos sob cada caractere da frase, deixando todas as letras minúsculas e excluido tudo que não for letra, removendo, assim, espaços e números
palavra = ''.join(char.lower() for char in entrada if char.isalpha())

if palavra[::-1] == palavra:
  print(f"A palavra {entrada} é um palíndromo")
else:
  print(f"A palavra {entrada} não é um palíndromo")
  