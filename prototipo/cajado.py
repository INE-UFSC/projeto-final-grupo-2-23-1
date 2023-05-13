import pygame as pg
from acessorio import Acessorio
from projetil import Projetil


# TODO: trocar nome da classe para Arma.
class Cajado(Acessorio, pg.sprite.Sprite):
    def __init__(self, nome, custo, descricao, tipo_projetil: Projetil):
        Acessorio.__init__(self, nome, custo, descricao)
        pg.sprite.Sprite.__init__(self)

        self.__tipo_projetil = tipo_projetil

        # TODO: adicionar mais armas e deixar o sprite customizável.
        arma_img = pg.image.load('./sprites/pistola_longa.png').convert_alpha()
        self.image = pg.transform.scale(arma_img, (70, 18))
        self.rect = self.image.get_rect()

        self.imagem_original = self.image

    def atirar_projetil(self, angulo: float):
        pass

    def rotacionar(self, angulo, pivo):
        '''Rotaciona a arma por um `angulo` ao longo de um `pivo`.'''

        if 90 < angulo < 270:
            self.image = pg.transform.rotozoom(self.imagem_original, 180 - angulo, 1)
            self.image = pg.transform.flip(self.image, True, False)
        else:
            self.image = pg.transform.rotozoom(self.imagem_original, angulo, 1)

        self.rect = self.image.get_rect(center = pivo)
