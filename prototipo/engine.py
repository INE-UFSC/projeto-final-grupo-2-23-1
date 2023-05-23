from enum import Enum
from time import perf_counter

import pygame as pg

from jogo import Jogo
from menu import Menu

# TODO: adicionar seletor de resolução e modo tela cheia no menu.
TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576


class Estado(Enum):
    MENU_PRINCIPAL = 0
    JOGO = 1

class Engine:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Éter Mortal')

        pg.display.set_mode((TELA_LARGURA, TELA_COMPRIMENTO))

        self.__jogo = Jogo()
        self.__menu = Menu()
        self.__estado = Estado.MENU_PRINCIPAL

    def iniciar(self):
        tempo_anterior = perf_counter()

        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit
            # dt é usado para garantir que, independentemente do FPS, os
            # movimentos do jogo permaneçam constantes e sincronizados.
            tempo_atual = perf_counter()
            dt = tempo_atual - tempo_anterior
            tempo_anterior = tempo_atual

            if self.__estado == Estado.MENU_PRINCIPAL:
                self.__menu.rodar()

                if self.__menu.iniciar_jogo:
                    self.__estado = Estado.JOGO
            elif self.__estado == Estado.JOGO:
                self.__jogo.rodar(dt)

            pg.display.flip()
