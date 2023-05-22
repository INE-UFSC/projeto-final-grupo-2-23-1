import pygame as pg
import random
from aerethor import Aerethor
from arma import Arma
from barra_status import BarraStatus
from capacete import Capacete
from jogador import Jogador
from projetil_linear import ProjetilLinear
from mapa import Objects

class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__background = pg.image.load('C:/Users/Pichau/Desktop/TyskaPOO/Jogo/projeto-final-grupo-2-23-1/prototipo/sprites/background.png')

        # TODO: o menu inicial deverá selecionar a arma e os equipamentos.
        proj_tipo = ProjetilLinear(5, 300, 3, 1)
        arma = Arma('Pistola longa', 0, '', proj_tipo)
        capacete = Capacete('Capacete militar', 0, '')

        self.hud = BarraStatus()

        self.__objects = Objects.draw()
        self.__jogador = Jogador(arma, capacete, (400, (self.__objects[1].rect.y)-2))

        self.__grupo_jogador = pg.sprite.Group(self.__jogador, capacete, arma)
        self.__grupo_projeteis_jogador = pg.sprite.Group()

        # TODO: melhorar geração de inimigos.
        self.__grupo_inimigos = pg.sprite.Group(Aerethor())

        self.__numero_rodada = 1
        self.__rodada_encerrada = False

    @property
    def numero_rodada(self):
        return self.__numero_rodada

    @property
    def rodada_encerrada(self):
        return self.__rodada_encerrada

    def rodar(self, dt):
        objects = Objects.draw()
        self.__tela.blit((self.__background), (0,0))
        if not self.__rodada_encerrada:
            self.ler_entrada()
            self.__grupo_jogador.update(dt)
            self.__grupo_projeteis_jogador.update(dt)
            self.__grupo_inimigos.update(self.__jogador.pos, dt)

        self.__grupo_jogador.draw(self.__tela)
        self.__grupo_projeteis_jogador.draw(self.__tela)
        self.__grupo_inimigos.draw(self.__tela)

        # TODO: realocar verificação de colisão para outro lugar.
        proj_colide_inimigo = pg.sprite.groupcollide(
            self.__grupo_inimigos,
            self.__grupo_projeteis_jogador,
            False, True
        )
        if proj_colide_inimigo is not None:
            for inimigo, projs in proj_colide_inimigo.items():
                for proj in projs:
                    inimigo.sofrer_dano(proj.dano)

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

        clique_esquerdo = pg.mouse.get_pressed()[0]
        if clique_esquerdo:
            proj = self.__jogador.atirar()

            if proj is not None:
                self.__grupo_projeteis_jogador.add(proj)

        self.__jogador.mover_mira(*pg.mouse.get_pos())

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False
