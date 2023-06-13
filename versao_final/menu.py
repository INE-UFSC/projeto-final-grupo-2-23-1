import pygame
import os

from button import Button
from capacete_militar import CapaceteMilitar
from math import sin, cos, pi, radians


class Menu:
    def __init__(self):
        self.__tela = pygame.display.get_surface()
        self.__background_color = (0, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__start_button = Button((0, 0, 0), self.__width/2 - 100, self.__height/2 + 150, 200, 100, 'Start')
        self.__titulo_button = Button((0, 0, 0), self.__width/2 - 80, self.__height/2 - 290, 200, 100, "Éter Mortal", fontsize = 90)
        self.__quit_button = Button((0,0,0), self.__width/2 + 380, self.__height/2 - 300, 200, 100, "X")
        self.__capacete_button = Button((0, 0, 0), self.__width/2 - 300 , self.__height/2 - 155, 0, 0, 'Capacete', fontsize = 40)
        self.__triangulo_D = pygame.transform.scale(pygame.image.load(os.path.join('imagens', 'triangulo.png')).convert(), (40, 40))
        self.__triangulo_E = pygame.transform.scale(pygame.image.load(os.path.join('imagens', 'triangulo.png')).convert(), (40, 40))
        self.__arma_button = Button((0, 0, 0), self.__width/2 - 300 , self.__height/2 + 80, 0, 0, 'Arma', fontsize = 40)

        


    def rodar(self):
        self.__tela.fill(self.__background_color)

        self.__start_button.draw(self.__tela)
        self.__titulo_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)
        self.__capacete_button.draw(self.__tela)
        self.__tela.blit(self.__triangulo_E, (100, 180))
        self.__tela.blit(self.__triangulo_D, (290, 180))
        self.__arma_button.draw(self.__tela)
        self.__tela.blit(self.__triangulo_E, (100, 400))
        self.__tela.blit(self.__triangulo_D, (290, 400))

        if self.__quit_button.clicked:
            raise SystemExit

        if self.__start_button.clicked:
            self.iniciar_jogo = True

        
