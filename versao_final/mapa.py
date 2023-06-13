import pygame as pg
from PIL import Image

# TODO: deve depender da resolução.
SPRITE_TAMANHO = 25


class Bloco(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((SPRITE_TAMANHO, SPRITE_TAMANHO))
        self.image.fill('#FFE3B3')
        self.rect = self.image.get_rect(topleft = pos)

def ler_bitmap(arquivo: str):
    img = Image.open(arquivo)

    (colunas, linhas) = img.size
    dados = list(img.getdata())

    mapa = pg.sprite.Group()
    jogador_pos = (-1, -1)
    for i in range(linhas):
        for j in range(colunas):
            val = dados[colunas*i + j]
            
            if val == 1:
                jogador_pos = (25*j, i*25)
            elif val == 2:
                mapa.add(Bloco((25*j, i*25)))

    # Jogador não está no mapa.
    if jogador_pos == (-1, -1):
        raise SystemError

    return (mapa, jogador_pos)
