import math
import json


def cria_input_cluster_7(n_pixels_x, n_pixels_y, R: 'raio', ptx, frequencia: 'GHz', pixel_size):
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
    cria_input_cluster_7(400, 400, 50, 43, 1.9, 10)