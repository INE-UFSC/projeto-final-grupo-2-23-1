import os
from enum import Enum
from time import perf_counter

import pygame as pg
from pygame import mixer

from fim_jogo import Fim
from jogador import MorteJogador
from jogo import Jogo
from menu import Menu
from menu_carta import MenuCarta

# TODO: adicionar seletor de resolução e modo tela cheia no menu.
TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576


class Estado(Enum):
    MENU_PRINCIPAL = 0
    JOGO = 1
    UPGRADE = 2
    FIM_DE_JOGO = 3

class Engine:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Éter Mortal')
        mixer.init()

        pg.display.set_mode((TELA_LARGURA, TELA_COMPRIMENTO))

        self.__jogo = Jogo()
        self.__menu_carta = MenuCarta(self.__jogo)
        self.__menu = Menu()
        self.__fim = Fim()
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
                    mixer.music.load(os.path.join('musica', 'trilha_jogo.wav'))
                    mixer.music.play(-1)

            elif self.__estado == Estado.JOGO:
                try:
                    self.__jogo.rodar(dt)
                except MorteJogador:
                    self.__estado = Estado.FIM_DE_JOGO

                if self.__jogo.rodada_encerrada:
                    self.__estado = Estado.UPGRADE

            elif self.__estado == Estado.UPGRADE:
                self.__menu_carta.rodar()

                if self.__menu_carta.pronto:
                    self.__jogo.iniciar_proxima_rodada()
                    self.__estado = Estado.JOGO

            elif self.__estado == Estado.FIM_DE_JOGO:
                self.__fim.rodar()

                if self.__fim.iniciar_jogo:
                    self.__estado = Estado.JOGO
                    del self.__jogo
                    self.__jogo = Jogo()

            pg.display.flip()
