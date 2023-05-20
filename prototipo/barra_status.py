import pygame as pg


class BarraStatus:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__fonte = pg.font.Font(None, 28)

    def atualizar_tela(self, vida_atual, vida_max, rodada_atual):
        self.__desenhar_numero_rodada(rodada_atual)
        self.__desenhar_barra_vida(vida_atual, vida_max)

    def __desenhar_numero_rodada(self, rodada):
        rodada_texto = self.__fonte.render(f'{rodada}', True, 'white')
        rodada_rect = rodada_texto.get_rect(topright = (
            self.__tela.get_width() - 50,
            25
        ))

        self.__tela.blit(rodada_texto, rodada_rect)

    def __desenhar_barra_vida(self, vida_atual, vida_max):
        vida_prop = vida_atual/vida_max

        pg.draw.rect(self.__tela, 'darkred', pg.Rect(50, 25, 250, 20), 2, 10)
        pg.draw.rect(self.__tela, 'red2', pg.Rect(55, 30, 240*vida_prop, 10), 0, 5)

        vida_texto = self.__fonte.render(f'{vida_atual}/{vida_max}', True, 'white')
        vida_rect = vida_texto.get_rect(midleft = (60, 35))

        self.__tela.blit(vida_texto, vida_rect)
