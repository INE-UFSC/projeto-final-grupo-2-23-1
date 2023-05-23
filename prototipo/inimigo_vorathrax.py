import os
from math import atan2, pi
from random import random

import pygame as pg

from entidade import Entidade


class Vorathrax(Entidade, pg.sprite.Sprite):
    '''Vorathrax e a versao mais forte do aerethor, mais resistente, maior e os seus tiros sao mais rapidos'''
    def __init__(self):
        Entidade.__init__(self, 25, 1, 3)
        pg.sprite.Sprite.__init__(self)

        self.__angulo = 0

        vorathrax_img = pg.image.load(os.path.join('sprites', 'vorathrax.png')).convert_alpha()

        self.image = pg.transform.scale(vorathrax_img, (40, 60))
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
        dif_jogador = jog_pos.x - self.__pos.x
        self.__pos.x += self.veloc_mov*dif_jogador*dt

        dif_linha = self.__linha_mestra - self.__pos.y
        if dif_linha != 0:
            self.__pos.y += dif_linha*dt

        self.__rotacionar(jog_pos)

        self.rect.center = round(self.__pos)
