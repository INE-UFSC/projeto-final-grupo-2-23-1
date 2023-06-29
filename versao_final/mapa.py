import os

import pygame as pg
from PIL import Image

SPRITE_TAMANHO = 25


class Bloco(pg.sprite.Sprite):
    def __init__(self, pos, textura=None):
        super().__init__()
        self.image = pg.Surface((SPRITE_TAMANHO, SPRITE_TAMANHO), pg.SRCALPHA)

        if textura is not None:
            self.image = pg.transform.scale(textura, (30, 30))

        self.rect = self.image.get_rect(topleft = pos)

class Mapa:
    def __init__(self, nome):
        self.textura = pg.image.load(os.path.join('imagens', f'chao_{nome}.png')).convert_alpha()

        background_img = pg.image.load(os.path.join('imagens', f'background_{nome}.png'))
        self.background = pg.transform.scale(background_img, (1024, 576))

        (self.blocos, self.jog_pos_inicial) = self.__ler_bitmap(os.path.join('mapas', f'{nome}.bmp'))

    def __ler_bitmap(self, arquivo: str):
        img = Image.open(arquivo)

        (colunas, linhas) = img.size
        dados = list(img.getdata())

        mapa = pg.sprite.Group()
        jogador_pos = (-1, -1)
        for i in range(linhas):
            mapa.add(Bloco((-SPRITE_TAMANHO + 10, i*SPRITE_TAMANHO)))
            mapa.add(Bloco((SPRITE_TAMANHO*colunas - 10, i*SPRITE_TAMANHO)))

            for j in range(colunas):
                val = dados[colunas*i + j]
                
                if val == 1:
                    jogador_pos = (SPRITE_TAMANHO*j, i*SPRITE_TAMANHO)
                elif val == 2:
                    mapa.add(Bloco((SPRITE_TAMANHO*j, i*SPRITE_TAMANHO), self.textura))

        # Jogador não está no mapa.
        if jogador_pos == (-1, -1):
            raise SystemError

        return (mapa, jogador_pos)
