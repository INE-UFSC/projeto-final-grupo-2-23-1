import pygame as pg
from button import Button
from engine import *




class Pause:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.__continuar_button = Button((255, 0, 0), self.__width/2 + 80, self.__height/2 + 200, 140, 40, 'Continuar', 40, True)
        self.__menu_button = Button((255, 0, 0), self.__width/2 - 150, self.__height/2 + 200, 70, 40, 'Menu', 40, True)
        self.continuar_jogo = False
        self.menu = False





    def pause(self):
        self.__continuar_button.draw(self.__tela)
        self.__menu_button.draw(self.__tela)


        if self.__continuar_button.clicked:
            self.continuar_jogo = True
        if self.__menu_button.clicked:
            self.menu = True