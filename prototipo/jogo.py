import pygame as pg

from arma import Arma
from barra_status import BarraStatus
from capacete import Capacete
from jogador import Jogador
from projetil_linear import ProjetilLinear


class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__grupo_sprites = pg.sprite.Group()

        # TODO: o menu inicial deverá selecionar a arma e os equipamentos.
        proj_tipo = ProjetilLinear(5, 300, 3, 1)
        arma = Arma('Pistola longa', 0, '', proj_tipo)
        capacete = Capacete('Capacete militar', 0, '')

        self.hud = BarraStatus()

        # TODO: definir a posição inicial do jogador através do mapa.
        self.__jogador = Jogador(arma, capacete, (400, 500))

        self.__grupo_sprites.add(self.__jogador)
        self.__grupo_sprites.add(capacete)
        self.__grupo_sprites.add(arma)

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
            self.ler_entrada()
            self.__grupo_sprites.update(dt)

        self.__grupo_sprites.draw(self.__tela)
        self.hud.atualizar_tela(self.__jogador.vida, self.__jogador.vida_max, self.__numero_rodada)

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

        if teclas[pg.K_q]:
            proj = self.__jogador.atirar()

            if proj is not None:
                self.__grupo_sprites.add(proj)

        (mouse_x, mouse_y) = pg.mouse.get_pos()
        self.__jogador.mover_mira(mouse_x, mouse_y)

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False
