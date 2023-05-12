import pygame as pg
from jogo import Jogo

# TODO: adicionar seletor de resolução e modo tela cheia no menu.
TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576

class Engine:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Zéfini')

        pg.display.set_mode((TELA_LARGURA, TELA_COMPRIMENTO))

        self.__clock = pg.time.Clock()
        self.__jogo = Jogo()

    def iniciar(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

            # dt é usado para garantir que, independentemente do FPS, os
            # movimentos do jogo permaneçam constantes e sincronizados.
            dt = self.__clock.tick()/1000

            self.__jogo.rodar(dt)

            pg.display.flip()
