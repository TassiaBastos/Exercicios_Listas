# Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

lista = ['t', 'a', 's', 's', 'i', 'a', 'l', 'a', 'i', 's']
vogais = ['a', 'e', 'i', 'o', 'u']
totConsoantes = 0
consoantes = []

for i in range(0, 10):
    if lista[i] not in vogais:
        consoantes.append(lista[i])
        totConsoantes += 1
print('Voce digitou %d consoantes' % totConsoantes)
print(consoantes)


# Pegando a informação do usuário:

listaChar = []
consoantes = 0
print ('Informe os caracters')
for i in range(10):
    listaChar.append((input('Caracter  '+ str(i+1) + ':\n')))
    char = listaChar[i]
    if(char not in ('a','e','i','o','u')):
        consoantes += 1
print(consoantes)