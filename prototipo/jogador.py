import pygame as pg
from entidade import Entidade


class Jogador(Entidade, pg.sprite.Sprite):
    def __init__(self, pos):
        Entidade.__init__(self, 30, 150, 1)
        pg.sprite.Sprite.__init__(self)

        jogador_img = pg.image.load("./sprites/jogador.png").convert_alpha()

        self.image = pg.transform.scale(jogador_img, (25, 50))
        self.rect = self.image.get_rect(midbottom = pos)

        self.__pos = pg.math.Vector2(self.rect.center)

        self.__mira_angulo = 0
        self.__aceleracao_vert = 0
        # Sentido horizontal que o jogador está andando.
        self.__sentido = 0

        # TODO: definir colisão com o chão ao invés de usar valor.
        self.CHAO = pos[1]

    def mover(self, sentido):
        self.__sentido = sentido

    def pular(self):
        if self.rect.bottom >= self.CHAO:
            self.__aceleracao_vert = -1

    def morrer(self):
        self.kill()

    def update(self, dt):
        '''Atualizar a posição do sprite do jogador.'''

        self.__pos.x += self.__sentido * self.veloc_mov * dt
        self.__pos.y += self.__aceleracao_vert

        self.rect.center = self.__pos

        if self.__aceleracao_vert != 0:
            self.__aceleracao_vert += 4*dt

        if self.rect.bottom > self.CHAO:
            self.rect.bottom = self.CHAO
            self.__pos.y = self.rect.centery
            self.__aceleracao_vert = 0
