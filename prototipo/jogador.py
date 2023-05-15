from math import atan2, pi

import pygame as pg

from entidade import Entidade


class Jogador(Entidade, pg.sprite.Sprite):
    # TODO: deixar configurável.
    # Altura do pulo em pixels.
    __ALTURA_PULO = 70
    # Tempo até alcançar a altura máxima (pico) do pulo em segundos.
    __TEMPO_PULO = 1/3

    # Usado como a aceleração vertical durante o pulo.
    __GRAVIDADE = (2*__ALTURA_PULO)/(__TEMPO_PULO**2)

    # Offset do sprite da arma em relação ao sprite do jogador.
    ARMA_OFFSET = (1, 6)

    def __init__(self, cajado, pos):
        Entidade.__init__(self, 30, 150, 1)
        pg.sprite.Sprite.__init__(self)

        self.__cajado = cajado

        jogador_img = pg.image.load("./sprites/jogador.png").convert_alpha()

        self.image = pg.transform.scale(jogador_img, (25, 50))
        self.rect = self.image.get_rect(midbottom = pos)

        self.__pos = pg.math.Vector2(self.rect.center)

        self.__mira_angulo = 0
        self.__veloc_vert = 0
        # Sentido horizontal que o jogador está andando.
        self.__sentido = 0

        # TODO: definir colisão com o chão ao invés de usar valor.
        self.CHAO = pos[1]

    def mover(self, sentido):
        self.__sentido = sentido

    def pular(self):
        if self.rect.bottom >= self.CHAO:
            self.__veloc_vert = -2*self.__ALTURA_PULO/self.__TEMPO_PULO

    def mover_mira(self, mira_x, mira_y):
        '''Move a mira e o ângulo da arma'''

        angulo = pi - atan2(
            self.__pos.y + self.ARMA_OFFSET[1] - mira_y,
            self.__pos.x + self.ARMA_OFFSET[0] - mira_x
        )

        # Para economizar recursos, somente rotacione se o ângulo diferir.
        if angulo != self.__mira_angulo:
            self.__mira_angulo = angulo

            self.__cajado.rotacionar(
                self.__mira_angulo*180/pi,
                self.__pos + self.ARMA_OFFSET
            )

    def morrer(self):
        self.kill()

    def update(self, dt):
        '''Atualiza a posição do sprite do jogador.'''

        self.__pos.x += self.__sentido * self.veloc_mov * dt
        # Método de Verlet assumindo aceleração constante para o cálculo da posição.
        self.__pos.y += self.__veloc_vert*dt + self.__GRAVIDADE*dt*dt/2

        self.rect.center = self.__pos

        if self.__veloc_vert != 0:
            self.__veloc_vert += self.__GRAVIDADE*dt

        if self.rect.bottom > self.CHAO:
            self.rect.bottom = self.CHAO
            self.__pos.y = self.rect.centery
            self.__veloc_vert = 0
