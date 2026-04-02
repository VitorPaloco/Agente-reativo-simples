def criar_labirinto():
    return [
        [1,1,1,1,1,1,1,1,1,1],
        [1,'E',0,0,1,0,0,0,0,1],
        [1,0,1,0,1,0,1,1,0,1],
        [1,0,1,0,0,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,1,1],
        [1,0,0,0,1,0,0,0,0,1],
        [1,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,0,0,'S',1],
        [1,1,1,1,1,1,1,1,1,1]
    ]

def imprimir_labirinto(lab):
    for linha in lab:
        for valor in linha:
            if valor == 1:
                print("█", end="")
            elif valor == 0:
                print(" ", end="")
            elif valor == 'E':
                print("E", end="")
            elif valor == 'S':
                print("S", end="")
            elif valor == 'R':
                print("R", end="")
        print()