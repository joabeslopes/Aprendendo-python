# Pula sapo, jogo que define se o sapo chega até o ultimo cano ou morre no caminho.
# Se baseia na altura maxima do pulo dele, tanto para cima quanto para baixo.
# O sapo começa no primeiro cano.

Pulo, NCanos = input("Digite a altura do pulo do sapo e o número de canos existentes: ").split()
AltCanos = input("Digite a altura individual de cada cano: ").split()

for i in range(0, int(NCanos)-1):
    if(abs(int(AltCanos[i+1]) - int(AltCanos[i])) > int(Pulo)):
        win = False
        break
    else:
        win = True

if win:
    print("YOU WIN")
else:
    print("GAME OVER")
