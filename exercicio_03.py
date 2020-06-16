# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [9.0, 7.5, 8.5, 10.0]
media = sum(notas)/len(notas)

print("Notas: ", notas)
print("Media: ", media)

# Pedindo a informação do usuário

listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(4):
    listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
    media += listaNotas[i]
media = media/4
print (listaNotas)
print (media)