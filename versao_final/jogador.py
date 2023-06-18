from math import atan2, pi

import pygame as pg

from entidade import Entidade


class MorteJogador(Exception):
    pass

class Jogador(Entidade, pg.sprite.Sprite):
    # TODO: deixar configurável.
    # Altura do pulo em pixels.
    __ALTURA_PULO = 70
    # Tempo até alcançar a altura máxima (pico) do pulo em segundos.
    __TEMPO_PULO = 1/3

    # Usado como a aceleração vertical durante o pulo.
    __GRAVIDADE = (2*__ALTURA_PULO)/(__TEMPO_PULO**2)

    # Offset do sprite da arma e do capacete em relação ao sprite do jogador.
    ARMA_OFFSET = (1, 6)
    CAPACETE_OFFSET = (0, -22)

    def __init__(self, arma, capacete, pos, objs_colisao):
        Entidade.__init__(self, 'jogador.png', pos, 30, 1, 150, 0.25)
        pg.sprite.Sprite.__init__(self)

        self.__arma = arma
        self.__capacete = capacete

        self.__veloc_vert = 0
        # Sentido horizontal que o jogador está andando.
        self.__sentido = 0

        # TODO: tirar os objetos do mapa daqui.
        self.__objs_colisao = objs_colisao

    def mover(self, sentido):
        self.__sentido = sentido

    def pular(self):
        for objeto in self.__objs_colisao.sprites():
            encima_horizontal = \
                objeto.rect.left <= self.rect.left <= objeto.rect.right or \
                objeto.rect.left <= self.rect.right <= objeto.rect.right

            if self.rect.bottom == objeto.rect.top and encima_horizontal:
                self.__veloc_vert = -2*self.__ALTURA_PULO/self.__TEMPO_PULO

    def mover_mira(self, mira_x, mira_y):
        '''Move a mira e o ângulo da arma'''

        angulo = pi - atan2(
            self.pos.y + self.ARMA_OFFSET[1] - mira_y,
            self.pos.x + self.ARMA_OFFSET[0] - mira_x
        )

        self.__arma.rotacionar(
            angulo,
            round(self.pos) + self.ARMA_OFFSET
        )

    def atirar(self):
        proj = self.__arma.atirar_projetil()

        return proj

    def update(self, dt):
        '''Atualiza a posição do sprite do jogador.'''

        super().update(dt)

        self.pos.x += self.__sentido * self.veloc_mov * dt
        self.rect.center = round(self.pos)

        colide_mapa = pg.sprite.spritecollide(self, self.__objs_colisao, False)
        if colide_mapa is not None:
            for objs in colide_mapa:
                if self.__sentido == -1:
                    self.rect.left = objs.rect.right
                elif self.__sentido == 1:
                    self.rect.right = objs.rect.left

                self.pos.x = self.rect.centerx
                break

        if self.__veloc_vert != 0:
            # Método de Verlet assumindo aceleração constante para o cálculo da posição.
            self.pos.y += self.__veloc_vert*dt + self.__GRAVIDADE*dt*dt/2
        self.__veloc_vert += self.__GRAVIDADE*dt

        self.rect.center = round(self.pos)

        colide_mapa = pg.sprite.spritecollide(self, self.__objs_colisao, False)
        if colide_mapa is not None:
            for objs in colide_mapa:
                if self.__veloc_vert < 0:
                    self.rect.top = objs.rect.bottom
                elif self.__veloc_vert > 0:
                    self.rect.bottom = objs.rect.top

                self.__veloc_vert = 0
                self.pos.y = self.rect.centery
                break

        self.__arma.rect.center = round(self.pos) + self.ARMA_OFFSET
        self.__capacete.rect.center = round(self.pos) + self.CAPACETE_OFFSET
