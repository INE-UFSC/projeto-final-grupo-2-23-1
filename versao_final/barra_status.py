import os

import pygame as pg


class BarraStatus:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__fonte = pg.font.Font(None, 36)
        self.__mostrados = []
        self.__upgrade_img = []
        self.__upgrades = {}

    def atualizar_barra(self, vida_atual, vida_max, eter, rodada_atual, upgrades):
        self.__desenhar_numero_rodada(rodada_atual)
        self.__desenhar_eter(eter)
        self.__desenhar_barra_vida(vida_atual, vida_max)
        self.__desenhar_upgrades(upgrades)

    def __desenhar_numero_rodada(self, rodada):
        rodada_texto = self.__fonte.render(f'{rodada}', True, 'white')
        rodada_rect = rodada_texto.get_rect(topright = (
            self.__tela.get_width() - 50,
            25
        ))

        self.__tela.blit(rodada_texto, rodada_rect)

    def __desenhar_eter(self, eter):
        fonte_eter = pg.font.Font(None, 30)

        eter_img = pg.image.load(os.path.join('sprites', 'eter.png'))
        eter_img = pg.transform.scale(eter_img, (22, 22))
        self.__tela.blit(eter_img, (self.__tela.get_width() - 75, 50))

        eter_texto = fonte_eter.render(f'{eter}', True, 'grey')
        eter_rect = eter_texto.get_rect(topright = (
            self.__tela.get_width() - 80,
            53
        ))

        self.__tela.blit(eter_texto, eter_rect)

    def __desenhar_barra_vida(self, vida_atual, vida_max):
        vida_prop = vida_atual/vida_max

        pg.draw.rect(self.__tela, 'darkred', pg.Rect(50, 25, 250, 20), 2, 10)
        pg.draw.rect(self.__tela, 'red2', pg.Rect(55, 30, 240*vida_prop, 10), 0, 5)

        vida_texto = self.__fonte.render(f'{int(vida_atual)}/{int(vida_max)}', True, 'white')
        vida_rect = vida_texto.get_rect(midleft = (60, 35))

        self.__tela.blit(vida_texto, vida_rect)

    def __desenhar_upgrades(self, upgrade):
        fonte_up = pg.font.Font(None, 25)
        upgrades = upgrade
        printed = []
        z = 0

        for upgrade in upgrades:
            num_upgrade = upgrades.count(upgrade)
            if upgrade not in self.__mostrados:
                self.__mostrados.append(upgrade)
                upgrade_image = pg.image.load(os.path.join('imagens', upgrade+'.png'))
                self.__upgrade_img.append(pg.transform.scale(upgrade_image, (30, 40)))
                self.__upgrades[upgrade] = [num_upgrade, self.__upgrade_img[-1]]

            if num_upgrade > 1:
                self.__upgrades[upgrade][0] = num_upgrade

        for upgrade in upgrades:
            if upgrade not in printed:
                printed.append(upgrade)
                self.__tela.blit(self.__upgrades[upgrade][1], (10 + z*35, 500))

                up_texto = fonte_up.render(f'{self.__upgrades[upgrade][0]}', True, 'black')
                up_rect = up_texto.get_rect(bottomleft = (36+z*35, 541))
                self.__tela.blit(up_texto, up_rect)
                z += 1
