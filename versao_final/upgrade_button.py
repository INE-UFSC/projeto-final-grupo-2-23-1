from typing import Any
import pygame as pg
import os
import random
from button import Button
from ler_txt import *


class UpgradeButton:
    def __init__(self):
        self.__upgrade_button = [0]*4
        self.__cartas = self.gerar_nomecarta()
        self.image = [0] * 4
        
    def buttons(self):
        for i in range(4):
            self.__image = pg.image.load(os.path.join('imagens', self.__cartas[i]))
            self.__upgrade_button[i] = Button((0,0,255), 37 + (i*200), 200, 150, 200, self.__cartas[i][:-4], fontsize=2)
            self.image[i] = pg.transform.scale(self.__image, (150,200))
        self.__image = pg.image.load(os.path.join('imagens', 'rerrol.png'))
        self.image.append(pg.transform.scale(self.__image, (150,200)))
        return(self.__upgrade_button, self.image)

    def gerar_nomecarta(self):

        palavras = []
        listanomes = []
        cartas = []    
        ler = LerTXT()
        
        listanomes.append(ler.ler('cartas.txt'))
        listanomes.append(ler.ler('cartas_inc.txt'))

        for i in range(2):
            for frase in listanomes[i]:
                palavras.extend(frase.split())

        while True:
            numero_aleatorio = random.randint(0, len(palavras)-1)
            if palavras[numero_aleatorio] not in cartas and '.png' in palavras[numero_aleatorio]:
                cartas.append(palavras[numero_aleatorio])
            if len(cartas) == 4:
                break
        return cartas
