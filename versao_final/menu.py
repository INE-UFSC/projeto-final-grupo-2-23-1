import os

import pygame

from arma import Arma
from button import Button
from capacetes_tipos import (CapaceteBob, CapaceteMilitar, CapaceteNinja,
                             CapaceteTyska)
from projetil_linear import ProjetilLinear


class Menu:
    def __init__(self):
        self.iniciar_jogo = False

        background_img = pygame.image.load(os.path.join('imagens', 'background_menu.jpg'))
        self.__background = pygame.transform.scale(background_img, (1024, 576))
        self.__tela = pygame.display.get_surface()

        self.__start_button = Button((0, 0, 0), 465, 386, 131, 63, ' ', 40, False)
        self.__quit_button = Button((0,0,0), 960, 13, 51, 56, " ", 40, False)

        self.__button_E_capacete = Button((200, 200, 200), 160, 214, 30, 40, ' ', 40, False)
        self.__button_D_capacete = Button((200, 200, 200), 282, 214, 30, 40, ' ', 40, False)
        self.__button_E_arma = Button((200, 200, 200), 160, 317, 30, 40, ' ', 40, False)
        self.__button_D_arma = Button((200, 200, 200), 282, 317, 30, 40, ' ', 40, False)
        self.__button_E_mapa = Button((200, 200, 200), 709, 183, 47, 47, ' ', 40, False)
        self.__button_D_mapa = Button((200, 200, 200), 865, 182, 47, 47, ' ', 40, False)

        rifle_proj = ProjetilLinear(15, 600, 2, (26, 255, 0))
        rifle = Arma('Rifle', 'rifle.png', 1.2, rifle_proj)
        ak_proj = ProjetilLinear(6, 450, 3, (252, 255, 46))
        ak47 = Arma('AK-47', 'ak47.png', 0.5, ak_proj)
        pistola_proj = ProjetilLinear(5, 300, 3, (0, 255, 255))
        pistola = Arma('Pistola', 'pistola.png', 0.75, pistola_proj)

        self.armas = [pistola, rifle, ak47]
        self.__arma_indice = 0
        self.arma_escolhida = self.armas[self.__arma_indice]

        self.capacetes = [CapaceteMilitar(), CapaceteNinja()]
        self.__capacete_indice = 0
        self.capacete_escolhido = self.capacetes[self.__capacete_indice]

        self.mapas = ['cidade', 'trincheira', 'arena']
        self.__mapa_indice = 0
        self.mapa_escolhido = self.mapas[self.__mapa_indice]

        self.__contadorb = self.__contadort = 0
        self.__firstb = False
    def rodar(self):
        self.__tela.blit(self.__background, (0, 0))

        self.__start_button.draw(self.__tela)
        self.__quit_button.draw(self.__tela)
        self.__button_D_arma.draw(self.__tela)
        self.__button_E_arma.draw(self.__tela)
        self.__button_D_capacete.draw(self.__tela)
        self.__button_E_capacete.draw(self.__tela)
        self.__button_D_mapa.draw(self.__tela)
        self.__button_E_mapa.draw(self.__tela)

        self.arma_escolhida = self.armas[self.__arma_indice]
        imagem_arma = self.arma_escolhida.image
        self.__tela.blit(imagem_arma, (200, 327))

        self.capacete_escolhido = self.capacetes[self.__capacete_indice]
        imagem_capacete = self.capacete_escolhido.image
        self.__tela.blit(imagem_capacete, (221, 212))

        self.mapa_escolhido = self.mapas[self.__mapa_indice]
        imagem_mapa = pygame.transform.scale(pygame.image.load(os.path.join('imagens', f'img_{self.mapa_escolhido}.png')).convert(), (228, 129))
        self.__tela.blit(imagem_mapa, (696, 239))

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_t]:
            self.__contadort = 1
        elif self.__contadort == 1 and teclas[pygame.K_y]:
            self.__contadort = 2
        elif self.__contadort == 2 and teclas[pygame.K_s]:
            self.__contadort = 3
        elif self.__contadort == 3 and teclas[pygame.K_k]:
            self.__contadort = 4
        elif self.__contadort == 4 and teclas[pygame.K_a]:
            self.capacetes.append(CapaceteTyska())
            self.__contadort = -1

        if not self.__firstb and teclas[pygame.K_b]:
            self.__contadorb = 1
            self.__firstb = True
        elif self.__contadorb == 1 and teclas[pygame.K_o]:
            self.__contadorb = 2
        elif self.__contadorb == 2 and teclas[pygame.K_b]:
            self.capacetes.append(CapaceteBob())
            self.__contadorb = -1

        if self.__button_D_arma.clicked:
            self.avancar_arma()

        if self.__button_E_arma.clicked:
            self.voltar_arma()

        if self.__button_D_capacete.clicked:
            self.avancar_capacete()

        if self.__button_E_capacete.clicked:
            self.voltar_capacete()

        if self.__button_D_mapa.clicked:
            self.avancar_mapa()

        if self.__button_E_mapa.clicked:
            self.voltar_mapa()

        if self.__quit_button.clicked:
            raise SystemExit

        if self.__start_button.clicked:
            self.iniciar_jogo = True

    def avancar_arma(self):
        self.__arma_indice = (self.__arma_indice + 1) % len(self.armas)

    def voltar_arma(self):
        self.__arma_indice = (self.__arma_indice - 1) % len(self.armas)

    def avancar_capacete(self):
        self.__capacete_indice = (self.__capacete_indice + 1) % len(self.capacetes)

    def voltar_capacete(self):
        self.__capacete_indice = (self.__capacete_indice - 1) % len(self.capacetes)

    def avancar_mapa(self):
        self.__mapa_indice = (self.__mapa_indice + 1) % len(self.mapas)

    def voltar_mapa(self):
        self.__mapa_indice = (self.__mapa_indice - 1) % len(self.mapas)
