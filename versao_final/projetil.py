from abc import ABC
import pygame as pg
from pygame import gfxdraw

class Projetil(ABC):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, cor, perfuracao: int):
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__cor = cor
        self.__perfuracao = perfuracao

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
    
    @property
    def perfuracao(self):
        return self.__perfuracao

class ProjetilConcreto(Projetil, pg.sprite.Sprite):
    def __init__(self, dano, veloc_proj, tamanho, cor, perfuracao, trajetoria, pos, angulo):
        Projetil.__init__(self, dano, veloc_proj, tamanho, cor, perfuracao)
        pg.sprite.Sprite.__init__(self)

        self.__angulo = angulo

        self.image = pg.Surface((2*self.tamanho + 1, 2*self.tamanho + 1), pg.SRCALPHA)
        gfxdraw.aacircle(
            self.image,
            self.tamanho, self.tamanho, self.tamanho,
            self.cor
        )
        gfxdraw.filled_circle(
            self.image,
            self.tamanho, self.tamanho, self.tamanho,
            self.cor
        )

        self.atualizar_trajetoria = trajetoria

        self.rect = self.image.get_rect(center = pos)
        self.mascara = pg.mask.from_surface(self.image)

        self.pos = pg.math.Vector2(self.rect.center)

    def esta_fora_tela(self):
        (largura_tela, altura_tela) = pg.display.get_window_size()

        fora_largura = self.rect.midright[0] < 0 or self.rect.midleft[0] > largura_tela
        fora_altura = self.rect.midbottom[1] < 0 or self.rect.midtop[1] > altura_tela

        return fora_largura or fora_altura

    def update(self, dt):
        self.pos += self.atualizar_trajetoria(dt, self.__angulo, self.veloc_proj)
        self.rect.center = self.pos

        if self.esta_fora_tela():
            self.kill()