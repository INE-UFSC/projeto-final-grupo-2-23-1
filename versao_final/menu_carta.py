import pygame as pg
import os
from button import Button
from nomes_cartas import *
from upgrade_button import UpgradeButton

UB = UpgradeButton()

class MenuCarta:
    def __init__(self):
        self.__pronto = False
        self.__selected = None
        self.__tela = pg.display.get_surface()
        self.__background_color = (0, 0, 0)
        self.__width = self.__tela.get_width()
        self.__height = self.__tela.get_height()
        self.iniciar_jogo = False
        self.__titulo_button = Button((0, 0, 0), 20, 20, 200, 100, "Upgrades", fontsize = 50)
        self.__upgrade_button, self.image = UB.buttons()
        self.__reroll_button = Button((0,0,255), 837, 200, 150, 200, "Rerrol", fontsize=2)
        self.__confirm_buttom = Button((0,0,100), self.__width/2 - 100, 500, 130, 50, "CONFIRM", fontsize=40)
    
    @property
    def pronto(self):
        return self.__pronto

    def rodar(self):
        self.__tela.fill(self.__background_color)
        self.__pronto = False
        self.__titulo_button.draw(self.__tela)
        self.__reroll_button.draw(self.__tela)
        self.__confirm_buttom.draw(self.__tela)
        
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
        
        if self.__reroll_button.clicked:
            #TODO verificar moeda do jogo

            self.__confirm_buttom.color = (0,0,100)
            UB = UpgradeButton()
            self.__upgrade_button, self.image = UB.buttons()
            self.__reroll_button.clicked = False
        
        if self.__confirm_buttom.clicked and (self.__selected != None):
            self.__pronto = True
            print(self.__selected.text)
            self.__confirm_buttom.clicked = False
            return None #self.__selected.text    
        else:
            self.__confirm_buttom.clicked = False
        
        


