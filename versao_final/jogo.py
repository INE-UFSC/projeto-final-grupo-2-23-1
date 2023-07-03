import os
from math import floor
from random import random

import pygame as pg
from pygame import mixer

from barra_status import BarraStatus
from inimigo import criar_Aerethor, criar_Vorathrax, criar_Xerthul, criar_Zylox, criar_Xandria, criar_Zorblax
from inimigo_grupo import InimigoGrupo
from jogador import Jogador, MorteJogador
from mapa import Mapa
from projetil_grupo import ProjetilGrupo


class Jogo:
    def __init__(self, arma, capacete, mapa, eter=0):
        mixer.music.load(os.path.join('musica', 'trilha_jogo.wav'))
        mixer.music.play(-1)
        self.__tela = pg.display.get_surface()

        self.hud = BarraStatus()

        self.__mapa = Mapa(mapa)
        jogador_pos = self.__mapa.jog_pos_inicial
        self.__jogador = Jogador(arma, capacete, jogador_pos)

        self.__grupo_projeteis_jogador = ProjetilGrupo()
        self.__grupo_jogador = pg.sprite.Group(self.__jogador, capacete, arma)

        self.__grupo_projeteis_inimigo = ProjetilGrupo()
        self.__grupo_inimigos = InimigoGrupo(self.__grupo_projeteis_inimigo)

        self.__numero_rodada = 0
        self.__rodada_encerrada = False
        self.__eter = eter
        self.__score = 0
        self.__score_eter = 150*random() + 150
        self.__upgrades = []

        self.iniciar_proxima_rodada()

    @property
    def numero_rodada(self):
        return self.__numero_rodada
    
    @property
    def score(self):
        return self.__score

    @property
    def rodada_encerrada(self):
        return self.__rodada_encerrada

    @property
    def jogador(self):
        return self.__jogador

    @property
    def upgrades(self):
        return self.__upgrades

    @upgrades.setter
    def upgrades(self, upgrade):
        self.__upgrades.append(upgrade)

    def rodar(self, dt):
        if self.__jogador not in self.__grupo_jogador:
            raise MorteJogador

        self.__tela.blit(self.__mapa.background, (0,0))
        if not self.__rodada_encerrada:
            self.ler_entrada()
            self.__grupo_jogador.update(dt, self.__mapa.blocos)
            self.__grupo_projeteis_jogador.update(dt, self.__mapa.blocos)
            self.__grupo_inimigos.update(dt, self.__jogador.pos, self.__mapa.blocos)
            self.__grupo_projeteis_inimigo.update(dt, self.__mapa.blocos)

        self.__mapa.blocos.draw(self.__tela)
        self.__grupo_jogador.draw(self.__tela)
        self.__grupo_projeteis_jogador.draw(self.__tela)
        self.__grupo_inimigos.draw(self.__tela)
        self.__grupo_projeteis_inimigo.draw(self.__tela)

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

                    if inimigo.groups() == []:
                        self.__score += inimigo.vida_total

                        self.__score_eter -= inimigo.vida_total

                        if self.__score_eter <= 0:
                            self.__score_eter = 150*random() + 150
                            self.__eter += 1

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

        self.hud.atualizar_tela(self.__jogador.vida_atual, self.__jogador.vida_total, self.__eter, self.__numero_rodada, self.__upgrades)

    def ler_entrada(self):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_a]:
            self.__jogador.mover(-1)
        elif teclas[pg.K_d]:
            self.__jogador.mover(1)
        else:
            self.__jogador.mover(0)

        if teclas[pg.K_SPACE]:
            self.__jogador.pular(self.__mapa.blocos)

        clique_esquerdo = pg.mouse.get_pressed()[0]
        if clique_esquerdo:
            proj = self.__jogador.atirar()

            if proj is not None:
                self.__grupo_projeteis_jogador.add(proj)

        self.__jogador.mover_mira(*pg.mouse.get_pos())

    def iniciar_proxima_rodada(self):
        self.__numero_rodada += 1
        self.__rodada_encerrada = False

        self.__grupo_projeteis_inimigo.empty()
        self.__grupo_projeteis_jogador.empty()

        num_aerethor = num_vorathrax = num_zylox = num_xerthul = num_xandria = num_zorblax = 0

        if self.__numero_rodada == 1:
            num_aerethor = floor(3)
        elif self.__numero_rodada == 2:
            num_aerethor = floor(4)
        elif self.__numero_rodada == 3:
            num_aerethor = floor(5)
        elif self.__numero_rodada == 4:
            num_aerethor = floor(6)
        elif self.__numero_rodada == 5:
            num_aerethor = floor(7)
        elif self.__numero_rodada == 6:
            num_aerethor = floor(6)
            num_vorathrax = floor(2)
        elif self.__numero_rodada == 7:
            num_aerethor = floor(6)
            num_vorathrax = floor(3)
        elif self.__numero_rodada == 8:
            num_aerethor = floor(5)
            num_vorathrax = floor(4)
        elif self.__numero_rodada == 9:
            num_aerethor = floor(5)
            num_vorathrax = floor(5)
        elif self.__numero_rodada == 10:
            num_vorathrax = floor(5)
            num_zorblax = floor(2)
        elif self.__numero_rodada == 11:
            num_vorathrax = floor(6)
            num_zorblax = floor(3)
        elif self.__numero_rodada == 12:
            num_vorathrax = floor(7)
            num_zorblax = floor(4)
        elif self.__numero_rodada == 13:
            num_vorathrax = floor(6)
            num_zorblax = floor(5)
        elif self.__numero_rodada == 14:
            num_vorathrax = floor(6)
            num_zorblax = floor(6)
        elif self.__numero_rodada == 15:
            num_zorblax = floor(6)
            num_zylox = floor(2)
            num_vorathrax = floor(4)
        elif self.__numero_rodada == 16:
            num_zorblax = floor(6)
            num_zylox = floor(3)
            num_vorathrax = floor(4)
        elif self.__numero_rodada == 17:
            num_zorblax = floor(7)
            num_zylox = floor(3)
            num_vorathrax = floor(3)
        elif self.__numero_rodada == 18:
            num_zorblax = floor(8)
            num_zylox = floor(4)
            num_vorathrax = floor(2)
        elif self.__numero_rodada == 19:
            num_zorblax = floor(10)
            num_zylox = floor(4)
            num_vorathrax = floor(2)
        elif self.__numero_rodada == 20:
            num_xerthul = floor(2)
            num_zorblax = floor(4)
            num_zylox = floor(4)
        elif self.__numero_rodada == 21:
            num_xerthul = floor(4)
            num_zorblax = floor(2)
            num_zylox = floor(4)
        elif self.__numero_rodada == 22:
            num_xerthul = floor(5)
            num_zorblax = floor(2)
            num_zylox = floor(5)
        elif self.__numero_rodada == 23:
            num_xerthul = floor(5)
            num_zorblax = floor(1)
            num_zylox = floor(5)
        elif self.__numero_rodada == 24:
            num_xerthul = floor(6)
            num_zylox = floor(6)
        elif self.__numero_rodada == 25:
            num_xerthul = floor(6)
            num_zylox = floor(2)
            num_xandria = floor(2)
        elif self.__numero_rodada == 26:
            num_xerthul = floor(6)
            num_zylox = floor(1)
            num_xandria = floor(3)
        elif self.__numero_rodada == 27:
            num_xerthul = floor(7)
            num_zylox = floor(1)
            num_xandria = floor(3)
        elif self.__numero_rodada == 28:
            num_xerthul = floor(8)
            num_zylox = floor(1)
            num_xandria = floor(4)
        elif self.__numero_rodada == 29:
            num_xerthul = floor(10)
            num_xandria = floor(5)
        else:
            num_aerethor = floor(0.15*self.__numero_rodada + 0.01*self.__numero_rodada**2 + 2)
            num_vorathrax = floor(0.15*self.__numero_rodada + 0.015*self.__numero_rodada**2)
            num_xerthul = floor(2 + 0.03*self.__numero_rodada + 0.001*self.__numero_rodada**2)
            num_zylox = floor(0.1*self.__numero_rodada + 0.001*self.__numero_rodada**2)
            num_zorblax = floor(self.__numero_rodada*0.1 + 1)
            num_xandria = floor(self.__numero_rodada*0.1)

        for _ in range(num_aerethor):
            self.__grupo_inimigos.add(criar_Aerethor())
        for _ in range(num_vorathrax):
            self.__grupo_inimigos.add(criar_Vorathrax())
        for _ in range(num_zylox):
            self.__grupo_inimigos.add(criar_Zylox())
        for _ in range(num_xerthul):
            self.__grupo_inimigos.add(criar_Xerthul())
        for _ in range(num_zorblax):
            self.__grupo_inimigos.add(criar_Zorblax())
        for _ in range(num_xandria):
            self.__grupo_inimigos.add(criar_Xandria())