import labirinto
import random
import time
import os


lab = labirinto.criar_labirinto()

def agente_reativo_simples(lab):

    robo = "R"
    robo_linha = 1
    robo_coluna = 1

    lab[robo_linha][robo_coluna] = robo

    for i in range(100):
        labirinto.imprimir_labirinto(lab)

        lab[robo_linha][robo_coluna] = 0
        movimentos = []
    
        if lab[robo_linha - 1][robo_coluna] != 1:
            movimentos.append((-1, 0)) # Cima
        if lab[robo_linha + 1][robo_coluna] != 1:
            movimentos.append((1, 0)) # Baixo
        if lab[robo_linha][robo_coluna - 1] != 1:
            movimentos.append((0, -1)) # Esquerda
        if lab[robo_linha][robo_coluna + 1] != 1:
            movimentos.append((0, 1)) # Direita

        nova_posicao = random.choice(movimentos)

        robo_linha += nova_posicao[0]
        robo_coluna +=nova_posicao[1]

        lab[robo_linha][robo_coluna] = robo

        time.sleep(1)
        os.system('clear')


def agente_reativo_estado_interno(lab):

    robo = "R"
    robo_linha = 1
    robo_coluna = 1

    visitados = set()  # Memória do agente

    lab[robo_linha][robo_coluna] = robo

    for i in range(100):
        labirinto.imprimir_labirinto(lab)

        # Marca posição atual como visitada
        visitados.add((robo_linha, robo_coluna))

        # Verifica se chegou na saída
        if lab[robo_linha][robo_coluna] == 'S':
            print("Saída encontrada!")
            break

        lab[robo_linha][robo_coluna] = 0

        movimentos = []
        movimentos_nao_visitados = []

        # CIMA
        if lab[robo_linha - 1][robo_coluna] != 1:
            movimentos.append((-1, 0))
            if (robo_linha - 1, robo_coluna) not in visitados:
                movimentos_nao_visitados.append((-1, 0))

        # BAIXO
        if lab[robo_linha + 1][robo_coluna] != 1:
            movimentos.append((1, 0))
            if (robo_linha + 1, robo_coluna) not in visitados:
                movimentos_nao_visitados.append((1, 0))

        # ESQUERDA
        if lab[robo_linha][robo_coluna - 1] != 1:
            movimentos.append((0, -1))
            if (robo_linha, robo_coluna - 1) not in visitados:
                movimentos_nao_visitados.append((0, -1))

        # DIREITA
        if lab[robo_linha][robo_coluna + 1] != 1:
            movimentos.append((0, 1))
            if (robo_linha, robo_coluna + 1) not in visitados:
                movimentos_nao_visitados.append((0, 1))

        # Prioriza caminhos não visitados
        if movimentos_nao_visitados:
            nova_posicao = random.choice(movimentos_nao_visitados)
        else:
            # Se não tiver opção, volta (evita travar)
            nova_posicao = random.choice(movimentos)

        robo_linha += nova_posicao[0]
        robo_coluna += nova_posicao[1]

        lab[robo_linha][robo_coluna] = robo

        time.sleep(1)
        os.system('clear')



os.system('clear')

# agente_reativo_simples(lab)
agente_reativo_estado_interno(lab)
