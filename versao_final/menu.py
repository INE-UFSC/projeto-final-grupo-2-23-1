import pygame
import os
from arma import Arma
from projetil_linear import ProjetilLinear
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
        self.__button_triangulo_D_capacete = Button((200, 200, 200), 290 , 180, 40, 40, ' ', fontsize = 40)
        self.__button_triangulo_E_capacete = Button((200, 200, 200), 100, 180, 40, 40, ' ', fontsize = 40)
        self.__button_triangulo_D_arma = Button((200, 200, 200), 290, 400, 40, 40, ' ', fontsize = 40)
        self.__button_triangulo_E_arma = Button((200, 200, 200), 100 , 400, 40, 40, ' ', fontsize = 40)
        self.__arma_button = Button((0, 0, 0), self.__width/2 - 300 , self.__height/2 + 80, 0, 0, 'Arma', fontsize = 40)
        rifle_proj = ProjetilLinear(15, 600, 2, (26, 255, 0), 1)
        rifle = Arma('Rifle', 'rifle.png', 1.2, rifle_proj)
        ak_proj = ProjetilLinear(6, 450, 3, (252, 255, 46), 1)
        ak47 = Arma('AK-47', 'ak47.png', 0.5, ak_proj)
        pistola_proj = ProjetilLinear(5, 300, 3, (0, 255, 255), 1)
        pistola = Arma('Pistola longa', 'pistola_longa.png', 0.75, pistola_proj)
        self.armas = [rifle, ak47, pistola]
        capacete_militar = CapaceteMilitar()
        self.capacetes = [capacete_militar]
        self.__imagem_arma_index = 0
        self.__imagem_capacete_index = 0
        

        


    def rodar(self):
        self.__tela.fill(self.__background_color)

        self.__start_button.draw(self.__tela)
        self.__titulo_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)
        self.__capacete_button.draw(self.__tela)
        self.__arma_button.draw(self.__tela)
        self.__button_triangulo_D_arma.draw(self.__tela)
        self.__button_triangulo_E_arma.draw(self.__tela)
        self.__button_triangulo_D_capacete.draw(self.__tela)
        self.__button_triangulo_E_capacete.draw(self.__tela)
        self.__tela.blit(self.__triangulo_E, (100, 180))
        self.__tela.blit(self.__triangulo_D, (290, 180))
        self.__tela.blit(self.__triangulo_E, (100, 400))
        self.__tela.blit(self.__triangulo_D, (290, 400))

        imagem_arma = self.armas[self.__imagem_arma_index].image
        self.__tela.blit(imagem_arma, (185, 410))

        imagem_capacete = self.capacetes[self.__imagem_capacete_index].image
        self.__tela.blit(imagem_capacete, (200, 180))
        
        if self.__button_triangulo_D_arma.clicked:
            self.avancar_arma()
        
        if self.__button_triangulo_E_arma.clicked:
            self.voltar_arma()

        if self.__button_triangulo_D_capacete.clicked:
            self.avancar_capacete()

        if self.__button_triangulo_E_capacete.clicked:
            self.voltar_capacete()
        
        if self.__quit_button.clicked:
            raise SystemExit

        if self.__start_button.clicked:
            self.iniciar_jogo = True

    def avancar_arma(self):
        if self.__imagem_arma_index >= len(self.armas) - 1:
            self.__imagem_arma_index = 0
        else:
            self.__imagem_arma_index += 1
        print(self.__imagem_arma_index)
        imagem = self.armas[self.__imagem_arma_index].image
        self.__tela.blit(imagem, (195, 400))
        
            
    def voltar_arma(self):
        if self.__imagem_arma_index == 0:
            self.__imagem_arma_index = len(self.armas) - 1
        else:
            self.__imagem_arma_index -= 1
        print(self.__imagem_arma_index)

    def avancar_capacete(self):
        if self.__imagem_capacete_index >= len(self.capacetes) - 1:
            self.__imagem_capacete_index = 0
        else:
            self.__imagem_capacete_index += 1
        print(self.__imagem_capacete_index)

    def voltar_capacete(self):
        if self.__imagem_capacete_index == 0:
            self.__imagem_capacete_index = len(self.capacetes) - 1
        else:
            self.__imagem_capacete_index -= 1
        print(self.__imagem_capacete_index)
        


            
        



        
