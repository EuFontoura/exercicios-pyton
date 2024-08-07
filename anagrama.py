# Crie um programa em Python que determine se duas palavras são anagramas.

palavra1 = input("insira a primeira palavra: ").lower()
palavra2 = input("insira a segunda palavra: ").lower()


lib1 = {}
lib2 = {}

for letra in palavra1:
  if letra in lib1:
    lib1[letra] += 1
  else:
    lib1[letra] = 1
    
for letra in palavra2:
  if letra in lib2:
    lib2[letra] += 1
  else:
    lib2[letra] = 1

if lib1 == lib2:
  print(f"as palavras {palavra1} e {palavra2} são anagramas")
else:
  print(f"as palavras {palavra1} e {palavra2} não são anagramas")
