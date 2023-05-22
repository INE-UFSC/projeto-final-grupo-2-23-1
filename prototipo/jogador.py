from math import atan2, pi

import pygame as pg

from entidade import Entidade
from mapa import Objects

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

    def __init__(self, arma, capacete, pos):
        Entidade.__init__(self, 30, 150, 1)
        pg.sprite.Sprite.__init__(self)

        self.__arma = arma
        self.__capacete = capacete

        jogador_img = pg.image.load("C:/Users/Pichau/Desktop/TyskaPOO/Jogo/projeto-final-grupo-2-23-1/prototipo/sprites/jogador.png").convert_alpha()

        self.image = pg.transform.scale(jogador_img, (25, 50))
        self.rect = self.image.get_rect(midbottom = pos)

        self.__pos = pg.math.Vector2(self.rect.center)

        self.__veloc_vert = 2
        # Sentido horizontal que o jogador está andando.
        self.__sentido = 0

        self.__objects = Objects.draw()

    @property
    def pos(self):
        return self.__pos

    def mover(self, sentido):
        self.__sentido = sentido

    def pular(self):
        for objects in self.__objects:
            if self.rect.colliderect(objects):
                self.__veloc_vert = -2*self.__ALTURA_PULO/self.__TEMPO_PULO
                
    def mover_mira(self, mira_x, mira_y):
        '''Move a mira e o ângulo da arma'''

        angulo = pi - atan2(
            self.__pos.y + self.ARMA_OFFSET[1] - mira_y,
            self.__pos.x + self.ARMA_OFFSET[0] - mira_x
        )

        self.__arma.rotacionar(
            angulo,
            round(self.__pos) + self.ARMA_OFFSET
        )

    def atirar(self):
        proj = self.__arma.atirar_projetil()

        return proj

    def morrer(self):
        self.kill()

    def update(self, dt):
        '''Atualiza a posição do sprite do jogador.'''

        self.__pos.x += self.__sentido * self.veloc_mov * dt

        if self.__veloc_vert != 0:
            # Método de Verlet assumindo aceleração constante para o cálculo da posição.
            self.__pos.y += self.__veloc_vert*dt + self.__GRAVIDADE*dt*dt/2
            self.__veloc_vert += self.__GRAVIDADE*dt

        self.rect.center = round(self.__pos)
       
        for objects in self.__objects:
            if self.rect.colliderect(objects):                   
                if self.rect.bottom >= (objects.rect.y)+1: 
                    if not(self.rect.x <= (objects.rect.left)-5) or not(self.rect.x >= (objects.rect.right)+5) :
                        self.rect.bottom = (objects.rect.y)+1
                        self.__pos.y = self.rect.centery
                        self.__veloc_vert = 1

        self.__arma.rect.center = round(self.__pos) + self.ARMA_OFFSET
        self.__capacete.rect.center = round(self.__pos) + self.CAPACETE_OFFSET
