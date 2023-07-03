import pygame as pg
from button import Button
import os


pg.init()
class Fim:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__background_color = (255, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__tente_button = Button((0, 0, 0), self.__width/2 + 0, self.__height/2 + 125, 370, 40, 'Tentar novamente')
        self.__quit_button = Button((0, 0, 0), self.__width/2 + 450, self.__height/2 - 270, 40, 40, "X")
        self.__fim_button = Button((0, 0, 0), self.__width/2 - 320, self.__height/2 - 200, 00, 00, "Fim de Jogo")
        self.__score_button = Button((0, 0, 0), self.__width/2 + 90, self.__height/2 - 150, 0, 0, "Score:")
        self.__menu_button = Button((0, 0, 0), self.__width/2 + 120, self.__height/2 + 55, 120, 40, 'Menu')
        self.__image = pg.image.load(os.path.join('imagens', 'Ceifador.png'))
        self.image = pg.transform.scale(self.__image, (200, 300))


    def rodar(self, score):
        self.__pontos_numero = Button((0, 0, 0), self.__width/2 + 235, self.__height/2 - 155, 0, 0, str(score))
        self.__tela.fill(self.__background_color)

        self.__tente_button.draw(self.__tela)
        self.__fim_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)
        self.__score_button.draw(self.__tela)
        self.__pontos_numero.draw(self.__tela)
        self.__menu_button.draw(self.__tela)
        self.__tela.blit(self.image, (200, 150))
        
        if self.__quit_button.clicked:
            raise SystemExit

        if self.__tente_button.clicked:
            self.iniciar_jogo = True

        self.menu_jogo = False
        if self.__menu_button.clicked:
            self.menu_jogo = True


