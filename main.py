from funcoes import *
import json


def main(nome):
    with open(os.path.join('input', nome)) as fp:
        config = json.load(fp)

    mapa = cria_mapa_prx_dB_de_celulas(config)

    if True:
        mapa_best_server = cria_mapa_id_best_server(mapa, config)
        desenha_mapa(mapa_best_server, nome, 'best_server')

    if True:
        mapa_cir = cria_mapa_cir(mapa, config)
        desenha_mapa(mapa_cir, nome, 'cir')
    
    if True:    
        for celula in config['celulas'].keys():
            mapa_celula = extrai_mapa(mapa, celula)
            desenha_mapa(mapa_celula, nome, celula)


if __name__ == '__main__':
    main('400x400-r50-10m-20dBm-1.9GHz-7cells.json')
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
