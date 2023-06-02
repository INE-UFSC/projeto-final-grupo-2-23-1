import pygame

#TODO: getters e setters e deixar modificavel

COLOR = (255, 100, 98)
SURFACE_COLOR = (20, 23, 26)
WIDTH = 1024
HEIGHT = 576
RED = (255, 0, 0)
WHITE = (255, 255, 255)
  
# Object class
class Bloco(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

# TODO: usar tilemap ao invés de valores hardcoded.
class Objects:
    def __init__(self):
        self.objects = []

        self.objects.append(Bloco(RED, 1000, 15)) #Limite da esquerda
        self.objects[len(self.objects)-1].rect.x = 0
        self.objects[len(self.objects)-1].rect.y = 0

        self.objects.append(Bloco(WHITE, 1000, 3000)) #Chao
        self.objects[len(self.objects)-1].rect.x = 15
        self.objects[len(self.objects)-1].rect.y = 560

        self.objects.append(Bloco(RED, 900, 15)) #Limite da direita
        self.objects[len(self.objects)-1].rect.x = 1009
        self.objects[len(self.objects)-1].rect.y = 0

        self.objects.append(Bloco(WHITE, 550, 150)) #Bloco maior da esquerda
        self.objects[len(self.objects)-1].rect.x = 15
        self.objects[len(self.objects)-1].rect.y = 489

        self.objects.append(Bloco(WHITE, 550, 200)) #Bloco menor da esquerda
        self.objects[len(self.objects)-1].rect.x = 150
        self.objects[len(self.objects)-1].rect.y = 525

        self.objects.append(Bloco(WHITE, 550, 200)) #Bloco menor da direita
        self.objects[len(self.objects)-1].rect.x = 625
        self.objects[len(self.objects)-1].rect.y = 525

        self.objects.append(Bloco(WHITE, 550, 200)) #Bloco maior da direita
        self.objects[len(self.objects)-1].rect.x = 809
        self.objects[len(self.objects)-1].rect.y = 489
