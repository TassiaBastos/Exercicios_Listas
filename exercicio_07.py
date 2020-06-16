# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = [1,2,3,4,5]
multip = 1
soma = 0
for i in vetor:
    multip *= i
    soma += i
print(vetor)
print('soma: ', soma)
print('multiplicacao', multip)

# Pegando a informação do usuário:
from pip._vendor.distlib.compat import raw_input

vetorNumeros = []
for i in range (0, 4):
    vetorNumeros.append( int (raw_input('Informe um numero inteiro: ')))
    soma = 0
    multiplicacao = 1
    for i in vetorNumeros:
        soma += i
        multiplicacao *= i
print(vetorNumeros)
print('Soma dos numeros:  %d ' % soma)
print('Multiplicacao dos numeros:  %d' % multiplicacao)
