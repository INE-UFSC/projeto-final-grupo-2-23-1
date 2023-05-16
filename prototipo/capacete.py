import pygame as pg

from acessorio import Acessorio


class Capacete(Acessorio, pg.sprite.Sprite):
    def __init__(self, nome, custo, descricao):
        Acessorio.__init__(self, nome, custo, descricao)
        pg.sprite.Sprite.__init__(self)

        # TODO: deixar o sprite customizável.
        capacete_img = pg.image.load('./sprites/capacete.png').convert_alpha()
        self.image = pg.transform.scale(capacete_img, (25, 35))
        self.rect = self.image.get_rect()
