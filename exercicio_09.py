# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.
from pip._vendor.distlib.compat import raw_input

vetor_A = []
for i in range(4):
    vetor_A.append(int(raw_input('Digite um numero: ')))
    somaQuadrados = 0
    for num in vetor_A:
        somaQuadrados += (num * num)

print('Numeros lidos: ', vetor_A)
print('A soma dos quadrados dos numeros lidos: ', somaQuadrados)
