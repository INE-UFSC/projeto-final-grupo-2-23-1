import pygame as pg
from button import Button
from engine import *




class Pause:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.__continuar_button = Button((0, 0, 0), self.__width/2 - 37, self.__height/2 + 100, 112, 60, 'Continuar', 40, False)
        self.__sair_button = Button((0, 0, 0), self.__width/2 - 37, self.__height/2 + 100, 112, 60, 'Sair', 40, False)





    def pause(self):
        loop = 1
        self.__continuar_button.draw(self.__tela)
        self.__sair_button.draw(self.__tela)
        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = 0
                

            pg.display.update()