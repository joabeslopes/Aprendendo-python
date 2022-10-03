'''
Programa que armazena os valores de uma matriz quadrada,
delimita a área da matriz que está acima da diagonal secundária,
e depois mostra a soma ou a média dos números que estão lá.

O exercício do beecrowd pede uma matriz 12x12, porém são muitos valores para
testar manualmente, então fiz esse exemplo 4x4 pois a lógica é a mesma, só mudar para 12.
'''

# Usuário digita S ou M para fazer a operação de soma ou média dos valores da área
O = input().upper()

# Define a estrutura da matriz
m = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(float(input())) # Usuário digita cada um dos valores das linhas separadamente
    m.append(linha)

area = 0
contador = 0

# A diagonal secundaria começa na última linha
secundaria = len(m)-1

for i in range(len(m)-1):
    for j in range(secundaria): # Faz a soma da área e conta quantos valores foram somados
        area = area +m[i][j]
        contador +=1
    secundaria -=1 # Vai reduzindo a área restante por conta da diagonal secundaria, ate chegar no ultimo valor

if O == 'S':
    print(f'{area:.1f}')
if O == 'M':
    print(f'{area/contador:.1f}')