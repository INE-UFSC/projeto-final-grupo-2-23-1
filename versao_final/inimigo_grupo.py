import pygame as pg


# Aqui estou usando o algoritmo Boids para os inimigos não se colidirem.
class InimigoGrupo(pg.sprite.Group):
    # Ajuste da velocidade
    COEFICIENTE_AFASTAMENTO = 0.025
    DISTANCIA_MINIMA = 35

    def __init__(self, grupo_projeteis_inimigo):
        super().__init__()

        self.__grupo_projeteis_inimigo = grupo_projeteis_inimigo

    def __atirar_projetil(self, inimigo, jog_pos):
        if inimigo.temporizador_ataque >= inimigo.tempo_recarga:
            inimigo.temporizador_ataque = 0

            if inimigo.tipo_projetil is not None:
                proj = inimigo.atirar(jog_pos)
                self.__grupo_projeteis_inimigo.add(proj)

    def __calcular_ajuste_colisao(self, inimigo):
        movimento_x = 0
        movimento_y = 0

        for outro_inimigo in self.sprites():
            if inimigo == outro_inimigo:
                continue

            dist = inimigo.pos.distance_to(outro_inimigo.pos)

            if dist < self.DISTANCIA_MINIMA:
                movimento_x += inimigo.pos.x - outro_inimigo.pos.x
                movimento_y += inimigo.pos.y - outro_inimigo.pos.y

        dx = movimento_x * self.COEFICIENTE_AFASTAMENTO
        dy = movimento_y * self.COEFICIENTE_AFASTAMENTO

        return pg.math.Vector2(dx, dy)

    def __colide_mapa(self, inimigo, mapa_objetos):
        colisao_objs = pg.sprite.spritecollide(inimigo, mapa_objetos, False)
        if colisao_objs is not None:
            for objs in colisao_objs:
                if objs.rect.x < inimigo.rect.x:
                    inimigo.rect.left = objs.rect.right
                else:
                    inimigo.rect.right = objs.rect.left

                inimigo.pos.x = inimigo.rect.centerx
                break

    def update(self, dt, jog_pos, mapa_objetos):
        for inimigo in self.sprites():
            inimigo.update(dt, jog_pos)
            inimigo.pos += self.__calcular_ajuste_colisao(inimigo)

            self.__atirar_projetil(inimigo, jog_pos)
            if (inimigo.dano == 0):
                self.__colide_mapa(inimigo, mapa_objetos)
