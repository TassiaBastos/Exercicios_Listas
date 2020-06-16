# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
from pip._vendor.distlib.compat import raw_input

vetor_1 = []
vetor_2 = []
vetor_3 = []

print('Informe os valores do primeiro vetor: ')
for i in range(10):
    vetor_1.append(int(raw_input('Digite um numero: ')))

print('Informe os valores do segundo vetor: ')
for i in range(10):
    vetor_2.append(int(raw_input('Digite um numero: ')))

for i in range(10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print('Vetor 1: ', vetor_1)
print('Vetor 2: ', vetor_2)
print('Vetor 3: ', vetor_3)
