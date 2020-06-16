# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
vetor.reverse()
print(vetor)

# Pedindo a informação do usuário:

vetorNumerosReais = []
print('Informe os 10 numeros reais')
for i in range(10):
    vetorNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
vetorNumerosReais.reverse()
print (vetorNumerosReais)