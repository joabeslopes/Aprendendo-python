# Calculadora que realiza conta de soma, subtração, multiplicação ou divisão.
print("CALCULADORA SIMPLES\n------------------\nDigite a conta desejada, com 1 espaço entre o número e o operador")
N1, operador, N2 = input(": ").split()
N1 = float(N1)
N2 = float(N2)

while(operador != '+' and operador != '-' and operador != '*' and operador != '/'): # Garante que o operador seja um desses 4
    print("Operador inválido! Digite novamente o operador(+ - * ou /)")
    operador = input(": ")
match operador: # Define qual será a conta, baseado no operador escolhido pelo usuário
    case '+':
        print(N1 + N2)
    case '-':
        print(N1 - N2)
    case '*':
        print(N1 * N2)
    case '/':
        print(N1 / N2)