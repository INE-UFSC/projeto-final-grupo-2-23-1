import pygame
import random
  
# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (20, 23, 26)
WIDTH = 0
HEIGHT = 0
RED = (255, 0, 0)
WHITE = (255, 255, 255)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
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

class Draw:
    def draw():
        objects = []

        objects.append(Sprite(RED, 900, 30))
        objects[len(objects)-1].rect.x = 0
        objects[len(objects)-1].rect.y = 0

        objects.append(Sprite(WHITE, 1000, 3000))
        objects[len(objects)-1].rect.x = 0
        objects[len(objects)-1].rect.y = 900

        objects.append(Sprite(RED, 900, 30))
        objects[len(objects)-1].rect.x = 1890
        objects[len(objects)-1].rect.y = 0

        objects.append(Sprite(WHITE, 550, 200))
        objects[len(objects)-1].rect.x = 30
        objects[len(objects)-1].rect.y = 700

        objects.append(Sprite(WHITE, 550, 300))
        objects[len(objects)-1].rect.x = 230
        objects[len(objects)-1].rect.y = 800

        objects.append(Sprite(WHITE, 550, 890))
        objects[len(objects)-1].rect.x = 1000
        objects[len(objects)-1].rect.y = 800

        objects.append(Sprite(WHITE, 550, 490))
        objects[len(objects)-1].rect.x = 1400
        objects[len(objects)-1].rect.y = 700

        return objects
  

pygame.init() 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    
    all_sprites_list.add(Draw.draw())
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()