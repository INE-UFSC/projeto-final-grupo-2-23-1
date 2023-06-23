import os

import pygame as pg


class Entidade(pg.sprite.Sprite):
    def __init__(self,
                 sprite_arquivo: str,
                 pos_inicial,
                 vida: int,
                 resistencia: float = 1,
                 veloc_mov: float = 3,
                 invulnerabilidade_periodo = 0.25):
        super().__init__()

        img = pg.image.load(os.path.join('sprites', sprite_arquivo)).convert_alpha()
        (altura_img, largura_img) = img.get_size()

        self.imagem_original = pg.transform.scale(img, (altura_img/10, largura_img/10))
        self.image = self.imagem_original

        self.__imagem_sem_dano = self.imagem_original
        colorImage = pg.Surface(self.imagem_original.get_size()).convert_alpha()
        colorImage.fill('red')
        self.__imagem_dano = pg.transform.scale(img, (altura_img/10, largura_img/10))
        self.__imagem_dano.blit(colorImage, (0,0), special_flags = pg.BLEND_RGBA_MULT)

        self.__vida_total = vida
        self.__vida_atual = vida
        self.__veloc_mov = veloc_mov
        self.__resistencia = resistencia

        self.__invulnerabilidade_periodo = invulnerabilidade_periodo
        self.__invulnerabilidade_temporizador = self.__invulnerabilidade_periodo

        self.rect = self.image.get_rect(midbottom = pos_inicial)
        self.mascara = pg.mask.from_surface(self.image)
        self.__pos = pg.math.Vector2(self.rect.center)

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    @property
    def vida_total(self):
        return self.__vida_total

    @property
    def vida_atual(self):
        return self.__vida_atual

    @property
    def veloc_mov(self):
        return self.__veloc_mov

    @veloc_mov.setter
    def veloc_mov(self, valor):
        self.__veloc_mov = valor

    @vida_total.setter
    def vida_total(self, valor):
        self.__vida_total = valor

    @vida_atual.setter
    def vida_atual(self, valor):
        self.__vida_atual = valor

    def sofrer_dano(self, dano: int):
        if dano <= 0:
            return

        if self.__invulnerabilidade_temporizador >= self.__invulnerabilidade_periodo:
            self.__vida_atual -= dano/self.__resistencia
            self.__invulnerabilidade_temporizador = 0

        if self.__vida_atual <= 0:
            self.kill()

    def update(self, dt):
        self.__invulnerabilidade_temporizador += dt

        if self.__invulnerabilidade_temporizador < self.__invulnerabilidade_periodo:
            self.imagem_original = self.image = self.__imagem_dano
        else:
            self.imagem_original = self.image = self.__imagem_sem_dano
