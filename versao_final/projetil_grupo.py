import pygame as pg


class ProjetilGrupo(pg.sprite.Group):
    def update(self, dt, mapa_blocos):
        pg.sprite.groupcollide(
            self,
            mapa_blocos,
            True, False
        )

        for proj in self.sprites():
            proj.update(dt)
