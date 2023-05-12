import pygame as pg


class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__grupo_sprites = pg.sprite.Group()

        self.__numero_rodada = 1
        self.__rodada_encerrada = False

    @property
    def numero_rodada(self):
        return self.__numero_rodada

    @property
    def rodada_encerrada(self):
        return self.__rodada_encerrada

    def rodar(self, dt):
        self.__tela.fill('black')
        self.__grupo_sprites.draw(self.__tela)

        if not self.__rodada_encerrada:
            self.ler_teclas()
            self.__grupo_sprites.update(dt)

    def ler_teclas(self):
        pass

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False
