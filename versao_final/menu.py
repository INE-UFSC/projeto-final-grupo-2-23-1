import pygame
import os

from button import Button
from pygame import mixer



class Menu:
    def __init__(self):
        self.__tela = pygame.display.get_surface()
        self.__background_color = (0, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__start_button = Button((0, 0, 0), self.__width/2 - 100, self.__height/2 + 150, 200, 100, 'Start')
        self.__titulo_button = Button((0, 0, 0), self.__width/2 - 80, self.__height/2 - 250, 200, 100, "Éter Mortal", fontsize = 90)
        self.__quit_button = Button((0,0,0), self.__width/2 + 380, self.__height/2 - 300, 200, 100, "X")
        self.__capacete_button = Button((0, 0, 0), self.__width/2 , self.__height/2 - 80, 0, 0, 'Capacete')


    def rodar(self):
        self.__tela.fill(self.__background_color)

        self.__start_button.draw(self.__tela)
        self.__titulo_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)
        self.__capacete_button.draw(self.__tela)

        if self.__quit_button.clicked:
            raise SystemExit

        if self.__start_button.clicked:
            self.iniciar_jogo = True
