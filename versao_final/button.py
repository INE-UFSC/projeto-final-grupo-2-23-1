from time import perf_counter

import pygame


class Button:
    TEMPO_MINIMO_SEGURAR = 0.75
    TEMPO_ENTRE_CLIQUES_SEGURANDO = 0.15

    def __init__(self, color, x,y,width,height, text='', fontsize = 60, is_drawable = True):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = None
        self.fontsize = fontsize
        self.clicked = False
        self.is_drawable = is_drawable

        self.__estava_segurando = False
        self.__segurar_temporizador = 0
        self.__clique_segurando_temporizador = 0

        self.__tempo_anterior = perf_counter()

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        if self.text != '':
            font = pygame.font.SysFont('', self.fontsize)
            self.textfont = font.render(self.text, 1, (255, 255, 255))
            self.rect = self.textfont.get_rect()
        if self.is_drawable:
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        win.blit(self.textfont, (self.x, self.y))
        self.click()

    def draw_text_centered(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        if self.text != '':
            font = pygame.font.SysFont('', self.fontsize)
            self.textfont = font.render(self.text, 1, (255, 255, 255))
            self.rect = self.textfont.get_rect()
        if self.is_drawable:
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        win.blit(self.textfont, (self.x + (self.width/2 - self.textfont.get_width()/2), self.y + (self.height/2 - self.textfont.get_height()/2)))
        self.click()

    def click(self):
        self.clicked = False
        click = pygame.mouse.get_pressed()[0]

        esta_segurando = self.__estava_segurando
        self.__estava_segurando = click

        if not click:
            self.__segurar_temporizador = 0
            self.__clique_segurando_temporizador = 0

            return

        mouse = pygame.mouse.get_pos()

        esta_mouse_dentro_botao = (self.x + self.width > mouse[0] > self.x) and (self.y + self.height > mouse[1] > self.y)

        if not esta_mouse_dentro_botao:
            # Não permita que o tempo que o usuário está clicando fora do botão conte.
            self.__segurar_temporizador = float('-inf')
            return

        tempo_atual = perf_counter()
        dt = tempo_atual - self.__tempo_anterior

        if esta_segurando:
            self.__segurar_temporizador += dt

        if not esta_segurando:
            self.clicked = True
        elif self.__segurar_temporizador > self.TEMPO_MINIMO_SEGURAR:
            self.__clique_segurando_temporizador %= self.TEMPO_ENTRE_CLIQUES_SEGURANDO
            self.__clique_segurando_temporizador += dt

            self.clicked = self.__clique_segurando_temporizador > self.TEMPO_ENTRE_CLIQUES_SEGURANDO

        self.__tempo_anterior = tempo_atual
