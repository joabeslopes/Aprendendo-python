# Algoritmo que ordena um vetor (lista numérica), do menor numero para o maior

numero = input("Digite os numeros inteiros que deseja ordenar: ").split()

for i in range(len(numero)-1):
# A variavel 'i' só precisa ir até o penúltimo valor, pois aí será comparada com o último 
    for j in range(i+1, len(numero)):

# é preciso converter os valores da lista para números
        numero[i] = int(numero[i])
        numero[j] = int(numero[j])
        
        if numero[i] > numero[j]:

# a variavel 'maior' serve apenas para fazer a troca dos valores
            maior = numero[i]
            numero[i] = numero[j]
            numero[j] = maior

print(numero)