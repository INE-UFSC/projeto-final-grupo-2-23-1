import pygame as pg

from cajado import Cajado
from jogador import Jogador


class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__grupo_sprites = pg.sprite.Group()

        # TODO: o menu inicial deverá selecionar a arma.
        cajado = Cajado('Pistola longa', 0, '', None)

        # TODO: definir a posição inicial do jogador através do mapa.
        self.__jogador = Jogador(cajado, (400, 450))

        self.__grupo_sprites.add(self.__jogador)
        self.__grupo_sprites.add(cajado)

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

        if not self.__rodada_encerrada:
            self.__grupo_sprites.update(dt)
            self.ler_entrada()

        self.__grupo_sprites.draw(self.__tela)

    def ler_entrada(self):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_a]:
            self.__jogador.mover(-1)
        elif teclas[pg.K_d]:
            self.__jogador.mover(1)
        else:
            self.__jogador.mover(0)

        if teclas[pg.K_SPACE]:
            self.__jogador.pular()

        (mouse_x, mouse_y) = pg.mouse.get_pos()
        self.__jogador.mover_mira(mouse_x, mouse_y)

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False
