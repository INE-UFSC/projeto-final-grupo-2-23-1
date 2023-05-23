from math import atan2, pi
from random import random

import pygame as pg

from entidade import Entidade
from projetil_linear import ProjetilLinear


class Aerethor(Entidade, pg.sprite.Sprite):
    '''Aerethor é o inimigo mais básico, ele voa e atira projéteis no jogador.'''

    def __init__(self):
        Entidade.__init__(self, 15, 1, 1)
        pg.sprite.Sprite.__init__(self)

        self.__angulo = 0

        aerethor_img = pg.image.load("./sprites/aerethor.png").convert_alpha()

        self.image = pg.transform.scale(aerethor_img, (30, 50))
        self.imagem_original = self.image

        (largura_tela, altura_tela) = pg.display.get_window_size()

        # Os inimigos movem-se sob essa linha.
        self.__linha_mestra = 0.3*altura_tela*random() + 0.2*altura_tela

        coluna_inicial = 0.2*largura_tela*random() + 0.4*largura_tela
        self.rect = self.image.get_rect(midbottom = (coluna_inicial, 0))
        self.mascara = pg.mask.from_surface(self.image)

        self.__pos = pg.math.Vector2(self.rect.center)
        self.__tipo_projetil = ProjetilLinear(5, 300, 3, 1)

    def __rotacionar(self, pos_ref):
        angulo = 3*pi/2 - atan2(
            self.__pos.y - pos_ref.y,
            self.__pos.x - pos_ref.x
        )

        if angulo == self.__angulo:
            return

        self.__angulo = angulo

        self.image = pg.transform.rotozoom(self.imagem_original, angulo*180/pi, 1)
        self.rect = self.image.get_rect(center = self.__pos)
        self.mascara = pg.mask.from_surface(self.image)

    def atirar(self, jog_pos):
        angulo = pi - atan2(
            self.__pos.y - jog_pos.y,
            self.__pos.x - jog_pos.x
        )
        proj = self.__tipo_projetil.criar_projetil(
            self.rect.center,
            angulo
        )

        return proj

    def morrer(self):
        self.kill()

    def update(self, jog_pos, dt):
        dif_jogador = jog_pos.x - self.__pos.x
        self.__pos.x += self.veloc_mov*dif_jogador*dt

        dif_linha = self.__linha_mestra - self.__pos.y
        if dif_linha != 0:
            self.__pos.y += dif_linha*dt

        self.__rotacionar(jog_pos)

        self.rect.center = round(self.__pos)
