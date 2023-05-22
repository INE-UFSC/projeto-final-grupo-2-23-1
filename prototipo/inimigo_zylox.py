from math import atan2, pi
from random import random

import pygame as pg

from entidade import Entidade

class Zylox(Entidade, pg.sprite.Sprite):
    '''Zylox sao os inimigos perseguidores, eles vao em direcao do jogador e so dao dano na base do contato'''
    def __init__(self):
        Entidade.__init__(self, 40, 0.5, 0)
        pg.sprite.Sprite.__init__(self)

        self.__angulo = 0

        zylox_img = pg.image.load("./sprites/zylox.png").convert_alpha()

        self.image = pg.transform.scale(zylox_img, (40, 60))
        self.image_original = self.image

        (largura_tela, altura_tela) = pg.display.get_window_size()

        self.__linha_mestra = 0.3*altura_tela*random() + 0.2*altura_tela

        coluna_inicial = 0.2*largura_tela*random() + 0.2*altura_tela
        self.rect = self.image.get_rect(midbottom = (coluna_inicial, 0))

        self.__pos = pg.math.Vector2(self.rect.center)

    def __rotacionar(self, pos_ref):
        angulo = 3*pi/2 - atan2(
            self.__pos.y - pos_ref.y,
            self.__pos.x - pos_ref.x
        )

        if angulo == self.__angulo:
            return
        
        self.__angulo = angulo

        self.image = pg.transform.rotozoom(self.image_original, angulo*180/pi, 1)
        self.rect = self.image.get_rect(center = self.__pos)

    def morrer(self):
        self.kill()

    def update(self, jog_pos, dt):
        dif_jogador_x = jog_pos.x - self.__pos.x
        self.__pos.x += self.veloc_mov*dif_jogador_x*dt

        dif_jogador_y = jog_pos.y - self.__pos.y
        self.__pos.y += self.veloc_mov*dif_jogador_y*dt

        self.__rotacionar(jog_pos)

        self.rect.center = round(self.__pos)