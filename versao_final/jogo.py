import os
from math import floor

import pygame as pg

from arma import Arma
from barra_status import BarraStatus
from capacete import Capacete
from inimigo_aerethor import Aerethor
from inimigo_grupo import InimigoGrupo
from inimigo_zylox import Zylox
from inimigo_vorathrax import Vorathrax
from inimigo_Xerthul import Xerthul
from jogador import Jogador, MorteJogador
from mapa import ler_bitmap
from projetil_linear import ProjetilLinear


class Jogo:
    def __init__(self):
        self.__tela = pg.display.get_surface()
        self.__background = pg.image.load(os.path.join('imagens', 'background_cidade.png'))

        # TODO: o menu inicial deverá selecionar a arma e os equipamentos.
        rifle_proj = ProjetilLinear(15, 600, 2, (26, 255, 0), 1)
        rifle = Arma('Rifle', 'rifle.png', 1.2, rifle_proj)

        ak_proj = ProjetilLinear(6, 450, 3, (252, 255, 46), 1)
        ak47 = Arma('AK-47', 'ak47.png', 0.5, ak_proj)

        pistola_proj = ProjetilLinear(5, 300, 3, (0, 255, 255), 1)
        pistola = Arma('Pistola longa', 'pistola_longa.png', 0.75, pistola_proj)

        arma = ak47

        capacete = Capacete('Capacete militar', 0, '')

        self.hud = BarraStatus()

        (self.__mapa, jogador_pos) = ler_bitmap('./mapas/cidade.bmp')
        self.__jogador = Jogador(arma, capacete, jogador_pos, self.__mapa)

        self.__grupo_jogador = pg.sprite.Group(self.__jogador, capacete, arma)
        self.__grupo_projeteis_jogador = pg.sprite.Group()

        self.__grupo_inimigos = InimigoGrupo()
        self.__grupo_projeteis_inimigo = pg.sprite.Group()

        self.__numero_rodada = 0
        self.__rodada_encerrada = False
        self.iniciar_proxima_rodada()

        self.__temporizador_inimigo = 0

    @property
    def numero_rodada(self):
        return self.__numero_rodada

    @property
    def rodada_encerrada(self):
        return self.__rodada_encerrada

    def rodar(self, dt):
        if self.__jogador not in self.__grupo_jogador:
            raise MorteJogador

        self.__temporizador_inimigo += dt

        if self.__temporizador_inimigo >= 1.5:
            self.__temporizador_inimigo = 0

            for inimigo in self.__grupo_inimigos:
                if not isinstance(inimigo, Zylox):
                    proj = inimigo.atirar(self.__jogador.pos)
                    self.__grupo_projeteis_inimigo.add(proj)

        self.__tela.blit((self.__background), (0,0))
        if not self.__rodada_encerrada:
            self.ler_entrada()
            self.__grupo_jogador.update(dt)
            self.__grupo_projeteis_jogador.update(dt)
            self.__grupo_inimigos.update(self.__jogador.pos, dt)
            self.__grupo_projeteis_inimigo.update(dt)
        

        self.__grupo_jogador.draw(self.__tela)
        self.__grupo_projeteis_jogador.draw(self.__tela)
        self.__grupo_inimigos.draw(self.__tela)
        self.__grupo_projeteis_inimigo.draw(self.__tela)
        self.__mapa.draw(self.__tela)
        

        # TODO: realocar verificação de colisão para outro lugar.
        proj_jog_colide_inimigo = pg.sprite.groupcollide(
            self.__grupo_inimigos,
            self.__grupo_projeteis_jogador,
            False, True,
            lambda a, b: b.mascara.overlap(
                a.mascara, ((a.rect.x - b.rect.x), (a.rect.y - b.rect.y))
            )
        )
        if proj_jog_colide_inimigo is not None:
            for inimigo, projs in proj_jog_colide_inimigo.items():
                for proj in projs:
                    inimigo.sofrer_dano(proj.dano)

        proj_inimigo_colide_jogador = pg.sprite.spritecollide(
            self.__jogador,
            self.__grupo_projeteis_inimigo,
            True,
            lambda a, b: b.mascara.overlap(
                a.mascara, ((a.rect.x - b.rect.x), (a.rect.y - b.rect.y))
            )
        )
        if proj_inimigo_colide_jogador:
            for proj in proj_inimigo_colide_jogador:
                self.__jogador.sofrer_dano(proj.dano)

        jogador_colide_inimigo = pg.sprite.spritecollide(
            self.__jogador,
            self.__grupo_inimigos,
            False,
            lambda a, b: b.mascara.overlap(
                a.mascara, ((a.rect.x - b.rect.x), (a.rect.y - b.rect.y))
            )
        )

        if jogador_colide_inimigo is not None:
            for inimigo in jogador_colide_inimigo:
                self.__jogador.sofrer_dano(inimigo.dano)

        if len(self.__grupo_inimigos) == 0:
            self.__rodada_encerrada = True


        self.hud.atualizar_tela(self.__jogador.vida, self.__jogador.vida_max, self.__numero_rodada)

    def ler_entrada(self):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_a]:
            self.__jogador.mover(-1)
        elif teclas[pg.K_d]:
            self.__jogador.mover(1)
        else:
            self.__jogador.mover(0)

        if teclas[pg.K_SPACE]:
            self.__jogador.pular()

        clique_esquerdo = pg.mouse.get_pressed()[0]
        if clique_esquerdo:
            proj = self.__jogador.atirar()

            if proj is not None:
                self.__grupo_projeteis_jogador.add(proj)

        self.__jogador.mover_mira(*pg.mouse.get_pos())

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False

        if self.__grupo_projeteis_inimigo is not None:
            self.__grupo_projeteis_inimigo.empty()

        if self.__numero_rodada < 5:
            self.num_aerethor = floor(1 + self.__numero_rodada*1)
            self.num_xerthul = floor(1 + self.__numero_rodada*1)

            for _ in range(self.num_aerethor):
                self.__grupo_inimigos.add(Aerethor())
            for _ in range(self.num_xerthul):
                self.__grupo_inimigos.add(Xerthul())

        elif self.__numero_rodada >= 5 and self.__numero_rodada < 10:
            self.num_aerethor = floor(7 - self.__numero_rodada*0.3)
            self.num_vorathrax = floor(0 + self.__numero_rodada*0.4)
            self.num_zylox = floor(0 + self.__numero_rodada*0.15)
            for _ in range(self.num_aerethor):
                self.__grupo_inimigos.add(Aerethor())
            
            for _ in range(self.num_vorathrax):
                self.__grupo_inimigos.add(Vorathrax())
            for _ in range(self.num_zylox):
                self.__grupo_inimigos.add(Zylox())