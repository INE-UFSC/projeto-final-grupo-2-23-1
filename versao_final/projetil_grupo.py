import pygame as pg


class ProjetilGrupo(pg.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, dt, mapa_objetos):
        pg.sprite.groupcollide(
            self,
            mapa_objetos,
            True, False
        )

        for proj in self.sprites():
            proj.update(dt)