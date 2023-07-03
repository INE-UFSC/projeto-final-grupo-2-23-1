import os

import pygame as pg
from PIL import Image

BLOCO_TAMANHO = 25


class Bloco(pg.sprite.Sprite):
    def __init__(self, pos, textura=None, tamanho=BLOCO_TAMANHO):
        super().__init__()
        self.image = pg.Surface((tamanho, tamanho), pg.SRCALPHA)

        if textura is not None:
            self.image = pg.transform.scale(textura, (30, 30))

        self.rect = self.image.get_rect(topleft = pos)

class Mapa:
    def __init__(self, nome, bloco_tamanho=BLOCO_TAMANHO):
        self.bloco_textura = pg.image.load(os.path.join('imagens', f'chao_{nome}.png')).convert_alpha()

        background_img = pg.image.load(os.path.join('imagens', f'background_{nome}.png'))
        self.background = pg.transform.scale(background_img, (1024, 576))
        self.bloco_tamanho = bloco_tamanho

        self.__carregar_mapa(os.path.join('mapas', f'{nome}.bmp'))

    def __carregar_mapa(self, arquivo: str):
        img = Image.open(arquivo)

        (colunas, linhas) = img.size
        dados = list(img.getdata())

        blocos = pg.sprite.Group()
        jogador_pos = (-1, -1)
        for i in range(linhas):
            blocos.add(Bloco((-self.bloco_tamanho + 10, i*self.bloco_tamanho)))
            blocos.add(Bloco((self.bloco_tamanho*colunas - 10, i*self.bloco_tamanho)))

            for j in range(colunas):
                val = dados[colunas*i + j]
                
                if val == 1:
                    jogador_pos = (self.bloco_tamanho*j, i*self.bloco_tamanho)
                elif val == 2:
                    blocos.add(Bloco((self.bloco_tamanho*j, i*self.bloco_tamanho), self.bloco_textura))

        # Jogador não está no mapa.
        if jogador_pos == (-1, -1):
            raise SystemError

        self.blocos = blocos
        self.jog_pos_inicial = jogador_pos
