import random
import time
import os

os.system('clear')

corredor = ["", "", "", "", "", "", "", "", "", ""]
robo = "R"
sujeira = "~"

posicoes_sujeira = random.sample(range(10), random.randint(2, 6))

for posicao in posicoes_sujeira:
    corredor[posicao] = sujeira

corredor[random.randint(0, 9)] = robo

for i in range(500):
    print(" | ".join(corredor))
    time.sleep(1)

    posicao_robo = corredor.index(robo)
    corredor[posicao_robo] = ""
    if posicao_robo == 0:
        corredor[posicao_robo + 1] = robo
    elif posicao_robo == 9:
        corredor[posicao_robo - 1] = robo
    else:
        nova_posicao = random.choice([posicao_robo - 1, posicao_robo + 1])
        corredor[nova_posicao] = robo