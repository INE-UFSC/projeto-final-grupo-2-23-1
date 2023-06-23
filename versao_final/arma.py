import os
from math import cos, pi, sin
from pygame import mixer
import pygame as pg

from acessorio import Acessorio
from projetil import Projetil


class Arma(Acessorio, pg.sprite.Sprite):
    def __init__(self, nome, custo, descricao, tipo_projetil: Projetil):
        Acessorio.__init__(self, nome, custo, descricao)
        pg.sprite.Sprite.__init__(self)

        self.__tipo_projetil = tipo_projetil

        self.__mira_angulo = 0

        # TODO: adicionar mais armas e deixar o sprite customizável.
        arma_img = pg.image.load(os.path.join('sprites', 'pistola_sprite.png')).convert_alpha()
        self.image = pg.transform.scale(arma_img, (50, 28))
        self.rect = self.image.get_rect()
        # Esse vetor determina em qual posição o projétil é lançado.
        self.tiro_pos = pg.math.Vector2(self.rect.topright)

        self.imagem_original = self.image

        # TODO: colocar tempo de recarga como um parâmetro.
        self.TEMPO_RECARGA = 0.75
        self.tiro_temporizador = self.TEMPO_RECARGA/2

    def atirar_projetil(self):
        if self.tiro_temporizador < self.TEMPO_RECARGA:
            return None

        self.tiro_temporizador = 0

        proj = self.__tipo_projetil.criar_projetil(
            self.tiro_pos,
            self.__mira_angulo
        )
        
        return proj

    def rotacionar(self, angulo, pivo):
        '''Rotaciona a arma por um `angulo` ao longo de um `pivo`.'''

        # Para economizar recursos, somente rotacione se o ângulo diferir.
        if angulo == self.__mira_angulo:
            return

        self.__mira_angulo = angulo
        angulo_graus = angulo*180/pi

        if 90 < angulo_graus < 270:
            self.image = pg.transform.rotozoom(self.imagem_original, 180 - angulo_graus, 1)
            self.image = pg.transform.flip(self.image, True, False)
        else:
            self.image = pg.transform.rotozoom(self.imagem_original, angulo_graus, 1)

        self.rect = self.image.get_rect(center = pivo)

    def update(self, dt):
        self.tiro_temporizador += dt

        # Determina se a arma está apontada para a direita (-1) ou esquerda (1).
        sentido = 1 if pi/2 < self.__mira_angulo < 3*pi/2 else -1

        # Calcula a posição em que o projétil é lançado após uma rotação da arma.
        # TODO: remover os valores hardcoded e parametrizar essa fórmula.
        self.tiro_pos = pg.math.Vector2(self.rect.center) + (
             35*cos(self.__mira_angulo) + sentido*7*sin(self.__mira_angulo),
            -35*sin(self.__mira_angulo) + sentido*7*cos(self.__mira_angulo) + 1)
