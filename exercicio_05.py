# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

vetorPar = []
vetorImpar = []
vetorNumeros = []
numero = 0

print('Informe os numeros:')
for i in range(20):
    vetorNumeros.append((int(input('Numero: ' + str(i + 1) + ':\n'))))
    numero = vetorNumeros[i]
    print(numero)
    if (numero % 2 == 0):
        vetorPar.append(numero)
    else:
        vetorImpar.append(numero)

print('Vetor original: ', vetorNumeros)
print('Vetor par: ', vetorPar)
print('Vetor impar: ', vetorImpar)
