import math
import json
import os


def cria_planeamento_hexagonal(n_pixels_x, n_pixels_y, R: 'raio em pixels', ptx, frequencia: 'GHz', pixel_size):
    """
    Para uma grelha de pixels e um raio de célula, cria um planeamento hexagonal de células
    retornando um JSON com coordenadas e configuração de cada célula

    :param n_pixels_x: numero de pixels no eixo dos x
    :param n_pixels_y: numero de pixels no eixo dos y
    :param R: Radio em pixels da célula
    :param ptx: potencia transmitida em dBm
    :param frequencia: frequencia de transmissão em GHz
    :param pixel_size: tamanho do pixel em metro

    :return: JSON com coordenadas e configuração de cada célula
    """
    
    
    r = int(math.sqrt(3)/2*R)
    celulas = {}
    n_celulas = 0

    x = 0
    y = 0

    while x <= n_pixels_x:
        y = 0
        while y <= n_pixels_y:
            i = str(n_celulas)
            celulas[i] = {'posicao': [x, y], 'ptx': ptx, 'frequencia': frequencia}
            n_celulas += 1
            y += 2 * r
        x += 3 * R

    x = 3 * R // 2
    y = r

    while x <= n_pixels_x:
        y = r
        while y <= n_pixels_y:
            i = str(n_celulas)
            celulas[i] = {'posicao': [x, y], 'ptx': ptx, 'frequencia': frequencia}
            n_celulas += 1
            y += 2 * r
        x += 3 * R


    config = {
        'celulas': celulas,
        'n_pixels_x': n_pixels_x,
        'n_pixels_y': n_pixels_y,
        'pixel_size': pixel_size,
    }

    nome_ficheiro = os.path.join('input', f'config-{n_pixels_x}x{n_pixels_y}-r{R}-{n_celulas}cells.json')
    with open(nome_ficheiro, 'w') as f:
        json.dump(config, f, indent=4)


def cria_input_cluster_7(n_pixels_x, n_pixels_y, R: 'raio', ptx, frequencia: 'GHz', pixel_size):
     """
    Cria um cluster de 7 células centrado numa grelha, inserindo um identificador para cada célula
    :param n_pixels_x:
    :param n_pixels_y:
    :param R:
    :param ptx:
    :param frequencia:
    :param pixel_size:
    :return:
    """
        
    r = int(math.sqrt(3) / 2 * R)

    posicao = {}
    centro_x = n_pixels_x // 2
    centro_y = n_pixels_y // 2

    posicao['1'] = [centro_x, centro_y]
    posicao['2'] = [centro_x, centro_y + 2 * r]
    posicao['3'] = [centro_x + R + r // 2, centro_y + r]
    posicao['4'] = [centro_x + R + r // 2, centro_y - r]
    posicao['5'] = [centro_x, centro_y - 2 * r]
    posicao['6'] = [centro_x - R - r // 2, centro_y + r]
    posicao['7'] = [centro_x - R - r // 2, centro_y - r]

    celulas = {}
    for i in range(1, 8):
        i = str(i)
        celulas[i] = {'posicao': posicao[i], 'ptx': ptx, 'frequencia': frequencia}

    config = {
        'celulas': celulas,
        'n_pixels_x': n_pixels_x,
        'n_pixels_y': n_pixels_y,
        'pixel_size': pixel_size,
    }

    with open(f"input\config-{n_pixels_x}x{n_pixels_y}-r{R}-7cells.json", 'w') as f:
        json.dump(config, f, indent=4)


if __name__ == '__main__':
  #  cria_input_cluster_7(400, 400, 50, 43, 1.9, 10)
    cria_planeamento_hexagonal(400, 400, 50, 43, 1.9, 10)
