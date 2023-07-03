import os

import pygame as pg


class Capacete(pg.sprite.Sprite):
    def __init__(self, nome, custo, descricao, img_arquivo, armadura, velocidade):
        super().__init__()

        self.__nome = nome
        self.__custo = custo
        self.__descricao = descricao
        self.__armadura = armadura
        self.__velocidade = velocidade

        capacete_img = pg.image.load(os.path.join('sprites', 'capacetes', img_arquivo)).convert_alpha()
        self.image = pg.transform.scale(capacete_img, (25, 35))
        self.rect = self.image.get_rect()

    @property
    def nome(self):
        return self.__nome

    @property
    def custo(self):
        return self.__custo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def armadura(self):
        return self.__armadura

    @property
    def velocidade(self):
        return self.__velocidade
