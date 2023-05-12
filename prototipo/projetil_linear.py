import pygame as pg
from projetil import Projetil
from math import cos, sin

class ProjetilLinear(Projetil, pg.sprite.Sprite):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int, angulo: float):
        Projetil.__init__(self, dano, veloc_proj, tamanho, perfuracao)
        pg.sprite.Sprite.__init__(self)

        self.angulo = angulo

        self.image = pg.Surface((10, 10))
        pg.draw.circle(self.image, 'white', (5,5), 5)
        self.rect = self.image.get_rect(center = (200, 200))
        self.pos = pg.math.Vector2(self.rect.center)

    def atualizar_trajetoria(self, dt):
        self.pos.x += cos(self.angulo)*self.veloc_proj*dt
        self.pos.y -= sin(self.angulo)*self.veloc_proj*dt

        self.rect.center = self.pos        

    def update(self, dt):
        self.atualizar_trajetoria(dt)

    def sofrer_impacto(self):
        self.kill()
