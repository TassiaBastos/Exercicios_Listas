# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = [1,2,3,4,5]
print(vetor)

# pedindo os valores do usuário:

vetorNumeros = []
print ('Informe os 5 numeros')
for i in range(5):
        vetorNumeros.append(input('Numero '+ str(i+1) + ':\n'))
print (vetorNumeros)