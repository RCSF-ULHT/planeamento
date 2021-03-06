import math
from math import log10
from matplotlib import pyplot as plt
import os
import seaborn as sns

sns.set()


def cria_mapa_vazio(size_x, size_y):
    return [[{} for _ in range(size_y)] for _ in range(size_x)]


def calcula_distancia(c_x, c_y, x, y, pixel_size):
    # cálculo da distancia entre dois pontos
    # usando o teorema de Pitágoras e a dimensão do pixe

    distancia = math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2) * pixel_size

    return distancia if distancia != 0 else pixel_size


def free_space(f: "frequencia [GHz]", d: "distancia [m]") -> "atenuação [dB]":
    """
        esta função recebe:
          - f:"frequencia [GHz]"
          - d:"distancia [m]"
        esta função retorna a atenuação de propagação em espaço livre [dB]
    """
    return 32.44 + 20 * math.log10(d / 1000) + 20 * math.log10(f * 1000)


def cria_mapa_prx_dB_de_celulas(config):
    """Cria mapa de potencia recebida em dB de um conjunto de celulas"""

    mapa = cria_mapa_vazio(config['n_pixels_x'], config['n_pixels_y'])

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):

            for celula, info in config['celulas'].items():
                c_x = info['posicao'][0]
                c_y = info['posicao'][1]

                distancia = calcula_distancia(c_x, c_y, x, y, config['pixel_size'])
                path_loss = free_space(info['frequencia'], distancia)
                prx = info['ptx'] - path_loss
                mapa[x][y][celula] = prx

    return mapa


def cria_mapa_id_best_server(mapa, config):
    mapa_cobertura = [[{} for _ in range(config['n_pixels_y'])] for _ in range(config['n_pixels_x'])]

    cor = {}
    for i, item in enumerate(list(config['celulas'])):
        cor[item] = i

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):
            p = mapa[x][y]
            celula = max(list(p.items()), key=lambda e: e[1])
            mapa_cobertura[x][y] = cor[celula[0]]

    return mapa_cobertura


def cria_mapa_cir(mapa, config):
    mapa_cir = [[None for _ in range(config['n_pixels_y'])] for _ in range(config['n_pixels_x'])]

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):
            mapa_cir[x][y] = cir(mapa[x][y])

    return mapa_cir


def cir(p):
    """
    calcula CIR de dicionario de prx[dBm] de celulas num ponto. considera C o melhor dos sinais.
    """

    lista_prx_dB_cells = list(p.values())
    lista_prx_dB_cells.sort(reverse=True)
    
    c_dB = lista_prx_dB_cells[0]  # best server signal strength
    lista_prx_dB_i_cells = lista_prx_dB_cells[1:]    # remaining received power levels
    
    soma_i_linear = 0
    for prx_dB_i_cell in lista_prx_dB_i_cells:
        soma_i_linear += 10**(prx_dB_i_cell/10)  # soma linear de px das celulas interferences
    soma_i_dB = 10*log10(soma_i_linear)

    cir_dB = c_dB - soma_i_dB
     
    return cir_dB


def extrai_mapa(mapa, celula):
    mapa_celula = []
    for linha in mapa:
        linha_celula = []
        for elemento in linha:
            linha_celula.append(elemento[celula])
        mapa_celula.append(linha_celula.copy())

    return mapa_celula


def desenha_mapa(mapa, nome, tipo):
    plt.clf()
    ax = sns.heatmap(mapa)
    caminho = os.path.join('output', f'{nome[:-5]}-{tipo}.png')
    plt.savefig(caminho)
