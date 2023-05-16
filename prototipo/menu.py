import pygame
from button import Button


Button_start = Button
pygame.init()
class Menu:
    def __init__(self):
        self.__res = (1024, 576)
        self.__screen = pygame.display.set_mode(self.__res)
        self.__color_light = (0, 0, 0)
        self.__color_dark = (0, 0, 0)
        self.__width = self.__screen.get_width()
        self.__height = self.__screen.get_height()
        self.__smallfont = pygame.font.SysFont('Arial',35)
        self.__text = self.__smallfont.render('start' , True , self.__color)
        self.__start_button = Button((0, 0, 0), self.__width/2 - 100, self.__height/2 - 125, 200, 100, 'Start') 
    
    def draw(self):
        self.__screen.fill((255,255,255))
        self.__start_button.draw(self.__screen)
        pygame.display.update()



MN = Menu()
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
	        pygame.quit()

    MN.draw()