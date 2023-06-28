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
from pause import Pause

TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576


class Estado(Enum):
    MENU_PRINCIPAL = 0
    JOGO = 1
    UPGRADE = 2
    FIM_DE_JOGO = 3
    PAUSE = 4

class Engine:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Éter Mortal')
        mixer.init()

        pg.display.set_mode((TELA_LARGURA, TELA_COMPRIMENTO))

        self.__menu = Menu()
        self.__fim = Fim()
        self.__estado = Estado.MENU_PRINCIPAL
        self.__pause = Pause()

        self.som_fim_jogo = mixer.Sound(os.path.join('musica', 'som_fim_jogo.wav'))

    def iniciar(self):
        tempo_anterior = perf_counter()
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit
                if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                    if self.__estado == Estado.JOGO:
                        self.__estado = Estado.PAUSE
                    elif self.__estado == Estado.PAUSE:
                        self.__estado = Estado.JOGO
                
                if self.__estado == Estado.JOGO:
                    mixer.Sound.stop(self.som_fim_jogo)

                if self.__estado == Estado.FIM_DE_JOGO:
                    mixer.Sound.play(self.som_fim_jogo)

                if self.__estado == Estado.MENU_PRINCIPAL:
                    mixer.Sound.stop(self.som_fim_jogo)



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

                    self.__menu.iniciar_jogo = False

            elif self.__estado == Estado.JOGO:
                try:
                    jogo.rodar(dt)

                    if jogo.pause == True:
                        self.__estado == Estado.PAUSE

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
                
                pg.mixer.music.pause()
                self.__fim.rodar(jogo.score)
                


                if self.__fim.iniciar_jogo:
                    self.__estado = Estado.JOGO
                    self.__fim.iniciar_jogo = False
                    del jogo
                    jogo = Jogo(self.__menu.arma_escolhida, self.__menu.capacete_escolhido)
                    mixer.music.load(os.path.join('musica', 'trilha_jogo.wav'))
                    mixer.music.play(-1)

                if self.__fim.menu_jogo:
                    del self.__menu
                    self.__menu = Menu()

                    self.__estado = Estado.MENU_PRINCIPAL
                    self.__fim.menu_jogo = False

            elif self.__estado == Estado.PAUSE:
                self.__pause.pause()
            
                if self.__pause.continuar_jogo:
                    self.__estado = Estado.JOGO
                    self.__pause.continuar_jogo = False

                if self.__pause.menu:
                    self.__estado = Estado.MENU_PRINCIPAL
                    self.__pause.menu = False
                
                



            pg.display.flip()
