import os

import pygame as pg

from button import Button


class Pause:
    def __init__(self):
        self.__tela = pg.display.get_surface()

        background_img = pg.image.load(os.path.join('imagens', 'background_pausa.png')).convert_alpha()
        self.__background = pg.transform.scale(background_img, (1024, 576))
        self.__tela.blit(self.__background, (0, 0))

        self.__continuar_button = Button((255, 0, 0), 400, 209, 226, 53, ' ', 40, False)
        self.__menu_button = Button((255, 0, 0), 365, 288, 296, 46, ' ', 40, False)
        self.continuar_jogo = False
        self.menu = False

    def pause(self):
        self.__continuar_button.draw(self.__tela)
        self.__menu_button.draw(self.__tela)

        if self.__continuar_button.clicked:
            self.continuar_jogo = True
        if self.__menu_button.clicked:
            self.menu = True
