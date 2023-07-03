import pygame as pg
import os
from button import Button

from upgrade_button import UpgradeButton
from upgrade import Upgrade
UB = UpgradeButton()

class MenuCarta:
    def __init__(self, jogo):
        self.__jogo = jogo
        self.__pronto = False
        self.__selected = None
        self.__tela = pg.display.get_surface()
        self.__background_color = (0, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__eter = Button((0, 0, 0), 20, 20, 200, 100, "UPGRADE", fontsize = 50)
        self.__titulo_button = Button((0, 0, 0), 20, 20, 200, 100, "UPGRADE", fontsize = 50)
        self.__upgrade_button, self.image = UB.buttons()
        self.__reroll_button = Button((0,0,255), 837, 200, 150, 200, "Rerrol", fontsize=2)
        self.__confirm_buttom = Button((0,0,100), self.__width/2 - 75, 500, 150, 50, "CONFIRM", fontsize=40)
        self.__text_confirmado = Button((0,0,0), self.__width/2 - 75, 450, 150, 50, "SELECIONE UM POWER UP", fontsize=40)
        self.__upgrade = Upgrade(jogo)

    @property
    def pronto(self):
        return self.__pronto

    def rodar(self):
        self.__tela.fill(self.__background_color)
        self.__pronto = False
        self.__titulo_button.draw(self.__tela)
        self.__reroll_button.draw(self.__tela)
        self.__confirm_buttom.draw_text_centered(self.__tela)
        self.__text_confirmado.draw_text_centered(self.__tela)

        for i in range(4):
            self.__upgrade_button[i].draw(self.__tela)
        
        for i in range(5):
            self.__tela.blit(self.image[i], (37 + (i*200), 200))
        

 #--------------------------------------\-----------------------------------\--------------------------
        for i in range(4):
            if self.__upgrade_button[i].clicked:
                self.__confirm_buttom.color = (0,0,255)
                self.__selected = self.__upgrade_button[i]
                self.__upgrade_button[i].clicked = False
                self.__text_confirmado.text = self.__selected.text
       
        
        if self.__reroll_button.clicked:
            if self.__jogo.eter > 0:
                self.__jogo.eter -= 1
                self.gerar_novos()

        if self.__confirm_buttom.clicked and (self.__selected != None):
            self.__pronto = True
            self.__upgrade.aplicar_upgrade(self.__selected.text)
            self.__jogo.upgrades.append(self.__selected.text)

            self.gerar_novos()
               
        else:
            self.__confirm_buttom.clicked = False
        
        fonte_eter = pg.font.Font(None, 30)

        eter_img = pg.image.load(os.path.join('sprites', 'eter.png'))
        eter_img = pg.transform.scale(eter_img, (22, 22))
        self.__tela.blit(eter_img, (self.__tela.get_width() - 75, 50))

        eter_texto = fonte_eter.render(f'{self.__jogo.eter}', True, 'grey')
        eter_rect = eter_texto.get_rect(topright = (
            self.__tela.get_width() - 80,
            53
        ))

        self.__tela.blit(eter_texto, eter_rect)



    def gerar_novos(self):
        UB = UpgradeButton()
        self.__selected = None
        self.__upgrade_button, self.image = UB.buttons()
        self.__confirm_buttom.color = (0,0,100)
        self.__confirm_buttom.clicked = False
        self.__reroll_button.clicked = False
        self.__text_confirmado.text = "SELECIONE UM POWER UP"

