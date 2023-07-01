import os

import pygame as pg

from capacete import Capacete


class CapaceteMilitar(Capacete):
    def __init__(self):
        Capacete.__init__(self, 'Capacete Militar', 2, 'Mais vida, menos velocidade')
        capacete_img = pg.image.load(os.path.join('sprites', 'capacete.png')).convert_alpha()
        self.image = pg.transform.scale(capacete_img, (25, 35))
        self.rect = self.image.get_rect()
        self.__velocidade = 1.5
        self.__armadura = 0.8
