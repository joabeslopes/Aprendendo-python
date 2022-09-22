# Contador de cédulas

valor = int(input("Digite um valor em reais: "))
print(valor)

notas = [100,50,20,10,5,2,1]

for nota in notas:
    qtNotas = valor // nota
    valor = valor % nota
    print(f"{qtNotas} nota(s) de R$ {nota},00")
