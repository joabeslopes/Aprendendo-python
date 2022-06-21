#   Bem vind@ ao python.
#   Com o python 3 instalado no seu computador, é possível executar os comandos aqui escritos,
# basta salvar seu arquivo de texto no formato .py, ir até o prompt de comando, e digitar "python3 nomeDoSeuArquivo.py" sem as aspas.

#   Recomendo fazer arquivos para os tópicos, um por vez, e ir executando para ver na prática o que acontece.

#   Note que esses comentários em vermelho não são executados pelo python, são apenas para leitura.

#---------------------------------------------------------------------------------------------------------#

#Tópico 1) Variáveis

#   Para criar variáveis com python, basta digitar o nome da variável e o conteúdo dela:

x = "Olá mundo"

#   Para mostrar o conteúdo da variável, é só imprimir o nome dela:
print(x)


#---------------------------------------------------------------------------------------------------------#

#Tópico 2) Operações matemáticas

#   Vamos fazer contas usando variáveis:
soma = 3+3
print("3 + 3 é:", soma)

subtracao = 15-8
print("15 - 8 é:", subtracao)

divisao = 14/2
print("14/2 é:", divisao)

multiplicacao = 5*2
print("5*2 é:", multiplicacao)

potencia = 3**2
print("3 elevado ao quadrado é:", potencia)

#   Para raiz quadrada é um pouco diferente, é preciso chamar uma função chamada math.sqrt e definir o número.

import math

raiz81 = math.sqrt(81)
print("raiz quadrada de 81:", raiz81)

#   Também dá para calcular a raiz usando a função math.pow, que vai elevar o número escolhido a uma fração,
# afinal é isso que significa calcular a raiz de um número.
#   É a mesma conta, feita de formas diferentes:

import math

raiz81 = math.pow(81, 1/2)
print("raiz quadrada de 81:", raiz81)


#---------------------------------------------------------------------------------------------------------#

#Tópico 3) Palavras (também chamadas de Strings)

#   O python, assim como qualquer outra linguagem, trabalha com letras e números.

palavra = "Palavra qualquer"

print(palavra)

#   Voce pode identificar qual letra está em determinada posição dentro da palavra, desta forma:

print(palavra [4])

#   Note que na 4ª posição ele encontrou a letra v, mesmo ela sendo na verdade a 5ª letra.
#   Isso acontece porque o python começa a contar as letras a partir do 0,
# então a letra "P" seria o elemento 0.


#---------------------------------------------------------------------------------------------------------#

#Tópico 4) Entrada de dados

#   Até agora, só trabalhamos com variáveis pré definidas, mas também podemos criar uma entrada de dados,
# para que o usuário digite, e desta forma o valor da variável será o que o usuário digitar.

nomeUsuario = input("Digite o seu nome: ")
print("Olá", nomeUsuario)
#   Note que no input podemos definir um texto que irá aparecer na tela, para o usuário saber o que queremos.


#---------------------------------------------------------------------------------------------------------#

#Tópico 5) Mudando o tipo de dados

#   Você já deve ter percebido que na programação existem vários tipos de dados,
# que podem ser números inteiros, números fracionários, palavras, etc.
#   E, apesar das variáveis no python só poderem receber um tipo de dado por vez,
# elas podem ser convertidas depois de criadas.

#   Isto é muito útil, por exemplo: a função input só recebe dados do tipo string (palavras),
# então se quisermos que seja um número, podemos converter a variável para um número, que
# pode ser inteiro (int), ou fracionário (float):

idade = input("Digite sua idade: ")
print( int(idade) )

#   Ou podemos fazer de um jeito mais fácil, que é convertendo diretamente a entrada do usuário:

idade = float( input("Digite sua idade: ") )
print(idade)
#   Note que o float mostra o número com casas decimais, já o int não.


#---------------------------------------------------------------------------------------------------------#

#   Agora que já viu o básico, está na hora de analisar os outros programas desse repositório,
# e com isso vai tendo uma base para criar seus próprios :)
