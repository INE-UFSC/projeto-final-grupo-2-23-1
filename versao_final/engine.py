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
                    jogo = Jogo(self.__menu.arma_escolhida, self.__menu.capacete_escolhido)
                    menu_carta = MenuCarta(jogo)

                    mixer.music.load(os.path.join('musica', 'trilha_jogo.wav'))
                    mixer.music.play(-1)

            elif self.__estado == Estado.JOGO:
                try:
                    jogo.rodar(dt)
                except MorteJogador:
                    self.__estado = Estado.FIM_DE_JOGO

                if jogo.rodada_encerrada:
                    self.__estado = Estado.UPGRADE

            elif self.__estado == Estado.UPGRADE:
                menu_carta.rodar()

                if menu_carta.pronto:
                    jogo.iniciar_proxima_rodada()
                    self.__estado = Estado.JOGO

            elif self.__estado == Estado.FIM_DE_JOGO:
                self.__fim.rodar()

                if self.__fim.iniciar_jogo:
                    self.__estado = Estado.JOGO
                    self.__fim.iniciar_jogo = False
                    del jogo
                    jogo = Jogo(self.__menu.arma_escolhida, self.__menu.capacete_escolhido)

            pg.display.flip()
