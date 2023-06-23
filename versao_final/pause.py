import pygame
from button import Button





class Pause:
    def __init__(self):
        self.__tela = pygame.display.get_surface()
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.__continuar_button = Button((0, 0, 0), self.__width/2 - 37, self.__height/2 + 100, 112, 60, 'Continuar', 40, False)
        self.__sair_button = Button((0, 0, 0), self.__width/2 - 37, self.__height/2 + 100, 112, 60, 'Sair', 40, False)





    def pause(self):
        loop = 1
        self.__continuar_button.draw(self.__tela)
        self.__sair_button.draw(self.__tela)
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = 0
            pygame.display.update()