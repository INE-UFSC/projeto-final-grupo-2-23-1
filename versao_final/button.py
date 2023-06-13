import pygame


class Button:
    def __init__(self, color, x,y,width,height, text='', fontsize = 60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = None
        self.fontsize = fontsize
        
        self.clicked = False

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        if self.text != '':
            font = pygame.font.SysFont('', self.fontsize)
            self.textfont = font.render(self.text, 1, (255, 255, 255))
            self.rect = self.textfont.get_rect()
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        win.blit(self.textfont, (self.x + (self.width/2 - self.textfont.get_width()/2), self.y + (self.height/2 - self.textfont.get_height()/2)))
        self.click()

    #deixar click mais preciso
    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.x + self.width > mouse[0] > self.x) and (self.y + self.height > mouse[1] > self.y):
            if (click[0] == True):
                # Melhorar aqui depois.
                self.clicked = True
                print('f')
