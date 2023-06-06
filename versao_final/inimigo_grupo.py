import pygame as pg

# Aqui estou usando o algoritmo Boids para os inimigos não se colidirem.
class InimigoGrupo(pg.sprite.Group):
    # Ajuste da velocidade
    COEFICIENTE_AFASTAMENTO = 0.025
    DISTANCIA_MINIMA = 35

    def __init__(self):
        super().__init__()

    def update(self, jog_pos, dt):
        for inimigo_sprite in self.sprites():
            movimento_x = 0
            movimento_y = 0

            inimigo_sprite.update(jog_pos, dt)

            for outro_inimigo in self.sprites():
                if inimigo_sprite == outro_inimigo:
                    continue

                dist = inimigo_sprite.pos.distance_to(outro_inimigo.pos)

                if dist < self.DISTANCIA_MINIMA:
                    movimento_x += inimigo_sprite.pos.x - outro_inimigo.pos.x
                    movimento_y += inimigo_sprite.pos.y - outro_inimigo.pos.y

            dx = movimento_x * self.COEFICIENTE_AFASTAMENTO
            dy = movimento_y * self.COEFICIENTE_AFASTAMENTO

            inimigo_sprite.pos += pg.math.Vector2(dx, dy)