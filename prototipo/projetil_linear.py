import pygame as pg
from projetil import Projetil
from math import cos, sin

class ProjetilLinear(Projetil):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        Projetil.__init__(self, dano, veloc_proj, tamanho, perfuracao)

    def criar_projetil(self, pos, angulo):
        proj = ProjetilLinearConcreto(self.dano, self.veloc_proj, self.tamanho, self.perfuracao, pos, angulo)

        return proj

    def sofrer_impacto(self):
        self.kill()

class ProjetilLinearConcreto(ProjetilLinear, pg.sprite.Sprite):
    def __init__(self, dano, veloc_proj, tamanho, perfuracao, pos, angulo):
        ProjetilLinear.__init__(self, dano, veloc_proj, tamanho, perfuracao)
        pg.sprite.Sprite.__init__(self)

        self.__angulo = angulo

        self.image = pg.Surface((10, 10))
        pg.draw.circle(self.image, 'aqua', (self.tamanho, self.tamanho), self.tamanho)
        self.rect = self.image.get_rect(center = pos)
        self.pos = pg.math.Vector2(self.rect.center)

    def atualizar_trajetoria(self, dt):
        self.pos.x += cos(self.__angulo)*self.veloc_proj*dt
        self.pos.y -= sin(self.__angulo)*self.veloc_proj*dt

        self.rect.center = self.pos

    def update(self, dt):
        self.atualizar_trajetoria(dt)