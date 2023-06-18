from math import atan2, pi
from random import random

import pygame as pg

from entidade import Entidade
from projetil_linear import ProjetilLinear


class Inimigo(Entidade, pg.sprite.Sprite):
    def __init__(self, stats, componente_inimigo, proj_tipo, tempo_recarga):
        (spr, vida, resistencia, veloc_mov) = stats
        (largura_tela, _) = pg.display.get_window_size()
        coluna_inicial = 0.6*largura_tela*random() + 0.2*largura_tela
        pos_inicial = (coluna_inicial, 0)

        Entidade.__init__(self, spr, pos_inicial, vida, resistencia, veloc_mov, 0.1)
        pg.sprite.Sprite.__init__(self)

        self.__componente_comportamento = componente_inimigo
        self.__tipo_projetil = proj_tipo

        self.__angulo = 0
        self.__tempo_recarga = tempo_recarga
        self.__temporizador_ataque = random() * 3*self.__tempo_recarga/4

    @property
    def temporizador_ataque(self):
        return self.__temporizador_ataque

    @temporizador_ataque.setter
    def temporizador_ataque(self, tempo):
        self.__temporizador_ataque = tempo

    @property
    def tipo_projetil(self):
        return self.__tipo_projetil

    @property
    def tempo_recarga(self):
        return self.__tempo_recarga

    def atirar(self, jog_pos):
        if self.__tipo_projetil is None:
            return

        angulo = pi - atan2(
            self.pos.y - jog_pos.y,
            self.pos.x - jog_pos.x
        )
        proj = self.__tipo_projetil.criar_projetil(
            self.rect.center,
            angulo
        )

        return proj

    def __rotacionar(self, pos_ref):
        angulo = 3*pi/2 - atan2(
            self.pos.y - pos_ref.y,
            self.pos.x - pos_ref.x
        )

        if angulo == self.__angulo:
            return

        self.__angulo = angulo

        self.image = pg.transform.rotozoom(self.imagem_original, angulo*180/pi, 1)
        self.rect = self.image.get_rect(center = self.pos)
        self.mascara = pg.mask.from_surface(self.image)

    def update(self, dt, jog_pos):
        super().update(dt)

        self.__temporizador_ataque += dt

        self.pos += self.__componente_comportamento.atualizar(dt, self, jog_pos)

        self.__rotacionar(jog_pos)

        self.rect.center = round(self.pos)

class VoadorComponente:
    def __init__(self, linha_amplitude, linha_base, dist_jogador):
        (largura_tela, altura_tela) = pg.display.get_window_size()

        # Os inimigos movem-se sob essa linha.
        self.__linha_mestra = linha_amplitude*altura_tela*random() + linha_base*altura_tela
        self.__dist_jogador = dist_jogador*largura_tela*random() - dist_jogador*largura_tela/2

    def atualizar(self, dt, obj, jog_pos):
        dif_jogador = jog_pos.x - self.__dist_jogador - obj.pos.x
        dx = 0
        if abs(dif_jogador) > 0:
            dx = obj.veloc_mov*dif_jogador*dt

        dif_linha = self.__linha_mestra - obj.pos.y
        dy = 0.75*dif_linha*dt

        return pg.math.Vector2(dx, dy)

def criar_Aerethor(nivel = 1):
    stats = ('aerethor.png', 15*nivel, nivel, 1.25)
    proj = ProjetilLinear(5, 200, 3, (255, 46, 255), 1)

    return Inimigo(stats, VoadorComponente(0.2, 0.2, 0.4), proj, 1.5)

def criar_Vorathrax(nivel = 1):
    stats = ('vorathrax.png', 35*nivel, 1.5*nivel, 0.6)
    proj = ProjetilLinear(10, 185, 5, (212, 243, 33), 2)

    return Inimigo(stats, VoadorComponente(0.15, 0.25, 0.4), proj, 2)

# TODO: adicionar inimigo camper.
#def criar_(nivel = 1):
#    stats = ('.png', 35*nivel, 1.5*nivel, 0.6)
#    proj = ProjetilLinear(12, 200, 8, (255, 24, 11), 3)
#
#    return Inimigo(stats, VoadorComponente(0.1, 0.1, 0.6), proj, 3.5)
