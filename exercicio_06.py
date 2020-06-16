# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
notasAcimaMedia = 0

for cont in range(10):
    media = 0
    soma = 0
    for cont1 in range(4):
        nota = float(input("Digite a nota: "))
        soma += nota
    media = soma / 4
    notas.append(media)
    print(notas)
for cont3 in notas:
    if (cont3 >= 7):
        notasAcimaMedia += 1
print('Total de alunos que obtiveram nota igual ou superior a 7.0: ', notasAcimaMedia)
