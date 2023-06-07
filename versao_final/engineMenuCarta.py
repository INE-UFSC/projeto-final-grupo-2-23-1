from time import perf_counter
import pygame as pg
from pygame import mixer
from menu_carta import MenuCarta


# TODO: adicionar seletor de resolução e modo tela cheia no menu.
TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576

class Engine2:
    def __init__(self):
        self.__menu = MenuCarta()

    def iniciar_menu_cartas(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit
        

            x = self.__menu.rodar()
            if x != (None):
                break
            pg.display.flip()
