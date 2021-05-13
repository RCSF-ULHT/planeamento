from funcoes import *
import json


def main(nome):
    with open(os.path.join('input', nome)) as fp:
        config = json.load(fp)

    mapa = cria_mapa(config)

    mapa_cobertura_celulas = cria_mapa_cobertura(mapa, config)
    desenha_mapa(mapa_cobertura_celulas, nome, 'all')

    for celula in config['celulas'].keys():
        mapa_celula = extrai_mapa(mapa, celula)
        desenha_mapa(mapa_celula, nome, celula)


if __name__ == '__main__':
    main('400x400-r100-3cells.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/