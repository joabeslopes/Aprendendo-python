#Bem vindo ao python. Para criar variáveis com ele, basta digitar o nome da variável e o conteúdo dela:

x = 6

#Vamos fazer contas colocando-as em variáveis:
soma = 3+3
sub = 15-8
div = 14/2
mult = 5*2
pot = 3**2

print("3 + 3 :", soma)
print("15 - 8 :", sub)
print("14/2 :", div)
print("5*2 :", mult)
print("3 elevado ao quadrado é:", pot)

#Para raiz quadrada é um pouco diferente, é preciso chamar uma função chamada math.sqrt e definir o número.
#Também dá para elevar o elemento a um número fracionário, que é um outro jeito de calcular raizes, usando o math.pow
#É a mesma conta feita de formas diferentes

import math

raiz1 = math.sqrt(81)
print("raiz quadrada de 81:", raiz1)

raiz2 = math.pow(81, 1/2)
print("raiz quadrada de 81:", raiz2)

#Vamos brincar com palavras agora.

palavra = "Palavras"

print(palavra)

#Voce pode identificar qual letra está em determinada posição dentro da palavra, usando os []
print(palavra [4])

#Ao executar, note que na 4ª posição ele encontrou a letra v, mesmo sendo na verdade a 5ª letra.
#Isto porque o python começa a contar a partir do 0, então a letra "P" é a letra 0.


#Vamos aprender agora sobre comparações e operadores lógicos.
