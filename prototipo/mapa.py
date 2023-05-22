import pygame
import random
#TODO: getters e setters e deixar modificavel

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (20, 23, 26)
WIDTH = 1024
HEIGHT = 576
RED = (255, 0, 0)
WHITE = (255, 255, 255)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
all_sprites_list = pygame.sprite.Group()
exit = True
clock = pygame.time.Clock()
  
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

class Objects:
    def draw():
        objects = []

        objects.append(Sprite(RED, 1000, 15)) #Limite da esquerda
        objects[len(objects)-1].rect.x = 0
        objects[len(objects)-1].rect.y = 0

        objects.append(Sprite(WHITE, 1000, 3000)) #Chao
        objects[len(objects)-1].rect.x = 15
        objects[len(objects)-1].rect.y = 560

        objects.append(Sprite(RED, 900, 15)) #Limite da direita
        objects[len(objects)-1].rect.x = 1009
        objects[len(objects)-1].rect.y = 0

        objects.append(Sprite(WHITE, 550, 150)) #Bloco maior da esquerda
        objects[len(objects)-1].rect.x = 15
        objects[len(objects)-1].rect.y = 489

        objects.append(Sprite(WHITE, 550, 200)) #Bloco menor da esquerda
        objects[len(objects)-1].rect.x = 150
        objects[len(objects)-1].rect.y = 525

        objects.append(Sprite(WHITE, 550, 200)) #Bloco menor da direita
        objects[len(objects)-1].rect.x = 625
        objects[len(objects)-1].rect.y = 525

        objects.append(Sprite(WHITE, 550, 200)) #Bloco maior da direita
        objects[len(objects)-1].rect.x = 809
        objects[len(objects)-1].rect.y = 489

        return objects
    
  
''''
pygame.init() 
all_sprites_list.add(Objects.draw())
all_sprites_list.update()
screen.fill(SURFACE_COLOR)
all_sprites_list.draw(screen)
pygame.display.flip()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    
   
    clock.tick(60)
  
pygame.quit()
'''