import pygame as pg
from jogador import Jogador


class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__grupo_sprites = pg.sprite.Group()

        # TODO: definir a posição inicial do jogador através do mapa.
        self.__jogador = Jogador(pos = (400, 450))
        self.__grupo_sprites.add(self.__jogador)

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
        teclas = pg.key.get_pressed()

        if teclas[pg.K_a]:
            self.__jogador.mover(-1)
        elif teclas[pg.K_d]:
            self.__jogador.mover(1)
        else:
            self.__jogador.mover(0)

        if teclas[pg.K_SPACE]:
            self.__jogador.pular()

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False
