import pygame
from button import Button
from pygame.locals import *
from app import *


#bg_img = pygame.image.load()
#bg_img = pygame.transform.scale(bg_img,(width,height))


Button_start = Button
pygame.init()
class Menu:
    def __init__(self):
        game_state = 'Menu'
        self.__res = (1024, 576)
        self.__screen = pygame.display.set_mode(self.__res)
        self.__background_color = (0, 0, 0)
        self.__width = self.__screen.get_width()
        self.__height = self.__screen.get_height()
        self.__start_button = Button((0, 0, 0), self.__width/2 - 100, self.__height/2 +125, 200, 100, 'Start', engine.iniciar)
        self.__titulo_button = Button((0, 0, 0), self.__width/2 - 80, self.__height/2 - 250, 200, 100, "Éter Mortal")
        self.__quit_button = Button((0,0,0), self.__width/2 + 380, self.__height/2 - 300, 200, 100, "X", exit)
    
    def draw(self):
        self.__screen.fill(self.__background_color)
        self.__start_button.draw(self.__screen)
        self.__titulo_button.draw(self.__screen)
        self.__quit_button.draw(self.__screen)
        pygame.display.update()

MN = Menu()
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
	        pygame.quit()
                
    MN.draw()


