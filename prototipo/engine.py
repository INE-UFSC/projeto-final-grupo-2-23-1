from time import perf_counter

import pygame as pg
from menu import Menu
from jogo import Jogo

# TODO: adicionar seletor de resolução e modo tela cheia no menu.
TELA_LARGURA = 1024
TELA_COMPRIMENTO = 576

class Engine:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Éter Mortal')

        pg.display.set_mode((TELA_LARGURA, TELA_COMPRIMENTO))

        self.__jogo = Jogo()

    def iniciar(self):
        self.ini_menu()
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

            self.__jogo.rodar(dt)

            pg.display.flip()


    def ini_menu(self):
        continues = True
        MN = Menu(((TELA_LARGURA, TELA_COMPRIMENTO)))
        while continues:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()        
            continues = MN.draw()
        return 
    
