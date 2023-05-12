import pygame
import random
  
# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (20, 23, 26)
WIDTH = 0
HEIGHT = 0
  
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
  
  
pygame.init()
  
RED = (255, 0, 0)
WHITE = (255, 255, 255)

  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Creating Sprite")
  
all_sprites_list = pygame.sprite.Group()



floor = (Sprite(WHITE, 1000, 3000))
floor.rect.x = 0
floor.rect.y = 900


limite_esquerda = (Sprite(RED, 900, 30))
limite_esquerda.rect.x = 0
limite_esquerda.rect.y = 0

limite_direita = (Sprite(RED, 900, 30))
limite_direita.rect.x = 1890
limite_direita.rect.y = 0


"""  
floor = []
x = 1920
y = 900
for i in range(3):
    floor.append(Sprite(WHITE, 1000, 100))
    floor[i].rect.x = x
    floor[i].rect.y = y
    x += 100
    y -= 100


x1 = 900
y1 = 900
for i in range(3):
    floor.append(Sprite(WHITE, 1000, 100))
    floor[i].rect.x = x1
    floor[i].rect.y = y1
    x1 += 100
    y1 -= 100



floor.append(Sprite(WHITE, 1000, 3000))
floor[len(floor)-1].rect.x = 0
floor[len(floor)-1].rect.y = 900



for i in range(len(floor)):  
    all_sprites_list.add(floor[i])
"""  

all_sprites_list.add(floor)
all_sprites_list.add(limite_esquerda)
all_sprites_list.add(limite_direita)
exit = True
clock = pygame.time.Clock()
  
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()