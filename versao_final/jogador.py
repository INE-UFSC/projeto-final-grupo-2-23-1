from math import atan2, pi

import pygame as pg

from capacete_bob import CapaceteBob
from capacete_tyska import CapaceteTyska
from entidade import Entidade


class MorteJogador(Exception):
    pass

class Jogador(Entidade, pg.sprite.Sprite):
    # Offset do sprite da arma e do capacete em relação ao sprite do jogador.
    ARMA_OFFSET = (2, 6)
    CAPACETE_OFFSET = (0, -18)

    def __init__(self, arma, capacete, pos_inicial):
        if isinstance(capacete, CapaceteTyska):
            pngjogador = 'corpotyska.png'
        elif isinstance(capacete, CapaceteBob):
            pngjogador = 'corpobob.png'
        else:
            pngjogador = 'soldado.png'

        Entidade.__init__(self, pngjogador, pos_inicial, 30, 1, 150, 0.25)
        pg.sprite.Sprite.__init__(self)

        # Altura do pulo em pixels.
        self.__ALTURA_PULO = 70
        # Tempo até alcançar a altura máxima (pico) do pulo em segundos.
        self.__TEMPO_PULO = 1/3
        # Usado como a aceleração vertical durante o pulo.
        self.__GRAVIDADE = (2*self.__ALTURA_PULO)/(self.__TEMPO_PULO**2)

        self.__arma = arma
        self.__capacete = capacete

        self.__veloc_vert = 0
        # Sentido horizontal que o jogador está andando.
        self.__sentido = 0
        self.__virado_para_esquerda = False

    @property
    def arma(self):
        return self.__arma

    @property
    def ALTURA_PULO(self):
        return self.__ALTURA_PULO

    @ALTURA_PULO.setter
    def ALTURA_PULO(self, ALTURA_PULO):
        self.__ALTURA_PULO = ALTURA_PULO
        self.GRAVIDADE

    @property
    def GRAVIDADE(self):
        return self.__GRAVIDADE

    @GRAVIDADE.setter
    def GRAVIDADE(self):
        self.__GRAVIDADE = (2*self.__ALTURA_PULO)/(self.__TEMPO_PULO**2)

    def mover(self, sentido):
        if (self.__virado_para_esquerda and sentido == 1) or \
        (not self.__virado_para_esquerda and sentido == -1):
            self.__virado_para_esquerda ^= True

            self.__capacete.image = pg.transform.flip(self.__capacete.image, True, False)
            self.imagem_dano = pg.transform.flip(self.imagem_dano, True, False)
            self.imagem_sem_dano = pg.transform.flip(self.imagem_sem_dano, True, False)

        self.image = self.imagem_sem_dano if not self.esta_com_dano else self.imagem_dano

        self.__sentido = sentido

    def pular(self, mapa_objetos):
        for objeto in mapa_objetos.sprites():
            encima_horizontal = \
                objeto.rect.left < self.rect.left < objeto.rect.right or \
                objeto.rect.left < self.rect.right < objeto.rect.right

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

    def update(self, dt, mapa_objetos):
        '''Atualiza a posição do sprite do jogador.'''

        super().update(dt)

        self.pos.x += self.__sentido * self.veloc_mov * dt
        self.rect.center = round(self.pos)

        colide_mapa = pg.sprite.spritecollide(self, mapa_objetos, False)
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

        colide_mapa = pg.sprite.spritecollide(self, mapa_objetos, False)
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
