from abc import ABC, abstractmethod

import pygame as pg
from pygame import gfxdraw


class Projetil(ABC):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, cor):
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__cor = cor

    @property
    def dano(self):
        return self.__dano
    @dano.setter
    def dano(self, valor):
        self.__dano = valor

    @property
    def veloc_proj(self):
        return self.__veloc_proj

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def cor(self):
        return self.__cor

    @abstractmethod
    def criar_projetil(self, pos, angulo):
        pass

class ProjetilConcreto(pg.sprite.Sprite):
    def __init__(self, dano, veloc_proj, tamanho, cor, trajetoria, pos, angulo):
        super().__init__()

        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__cor = cor

        self.__angulo = angulo

        self.image = pg.Surface((2*self.__tamanho + 1, 2*self.__tamanho + 1), pg.SRCALPHA)
        gfxdraw.aacircle(
            self.image,
            self.__tamanho, self.__tamanho, self.__tamanho,
            self.__cor
        )
        gfxdraw.filled_circle(
            self.image,
            self.__tamanho, self.__tamanho, self.__tamanho,
            self.__cor
        )

        self.atualizar_trajetoria = trajetoria

        self.rect = self.image.get_rect(center = pos)
        self.mascara = pg.mask.from_surface(self.image)

        self.pos = pg.math.Vector2(self.rect.center)

    @property
    def dano(self):
        return self.__dano

    def esta_fora_tela(self):
        (largura_tela, altura_tela) = pg.display.get_window_size()

        fora_largura = self.rect.midright[0] < 0 or self.rect.midleft[0] > largura_tela
        fora_altura = self.rect.midbottom[1] < 0 or self.rect.midtop[1] > altura_tela

        return fora_largura or fora_altura

    def update(self, dt):
        self.pos += self.atualizar_trajetoria(dt, self.__angulo, self.__veloc_proj)
        self.rect.center = self.pos

        if self.esta_fora_tela():
            self.kill()
