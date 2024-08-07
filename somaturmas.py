### Crie um programa em python que retorne a média de nota da turma, o numero de aprovados e o numero de reprovados ###

notas_turma = [90, 15, 45, 67, 69, 70, 95]
nota_aprovacao = 60
aprovados = 0
reprovados = 0

total = sum(notas_turma)
#é preciso converter a media em int para que não dê um número enorme após a vírgula
media = int(total/len(notas_turma))

for nota in notas_turma:
  if nota > nota_aprovacao:
    aprovados += 1 
  else:
    reprovados += 1

print(f"a média da turma é de: {media}")
print(f"o número de alunos aprovados são: {aprovados}")
print(f"o número de alunos reprovados são: {reprovados}")