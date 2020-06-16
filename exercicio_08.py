# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
from pip._vendor.distlib.compat import raw_input

pessoas = []
for i in range(3):
    pessoa = []
    pessoa.append(raw_input('Informe a idade da pessoa: '))
    pessoa.append(raw_input('Informe a altura da pessoa: '))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print('Idade: %s - Altura:  %s' %(pessoa[0], pessoa[1]))

