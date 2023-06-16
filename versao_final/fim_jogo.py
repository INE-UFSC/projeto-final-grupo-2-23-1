import pygame as pg
from button import Button
import os


pg.init()
class Fim:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__background_color = (0, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__tente_button = Button((0, 0, 0), self.__width/2 + 0, self.__height/2 + 0, 200, 100, 'Tentar novamente')
        self.__quit_button = Button((0, 0, 0), self.__width/2 + 380, self.__height/2 - 300, 200, 100, "X")
        self.__fim_button = Button((0, 0, 0), self.__width/2 - 10, self.__height/2 - 100, 200, 100, "Fim de Jogo")
        self.__image = pg.image.load(os.path.join('imagens', 'Sprite-morte.png'))
        self.image = pg.transform.scale(self.__image, (200,300))


    def rodar(self):
        self.__tela.fill(self.__background_color)

        self.__tente_button.draw(self.__tela)
        self.__fim_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)

        self.__tela.blit(self.image, (200, 150))
        
        if self.__quit_button.clicked:
            raise SystemExit

        if self.__tente_button.clicked:
            self.iniciar_jogo = True

