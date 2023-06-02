from abc import ABC, abstractmethod


class Entidade(ABC):
    def __init__(self, vida_inicial: int, veloc_mov: float, veloc_tiro: float, invic_cooldown: float):
        self.__vida_max = vida_inicial
        self.__vida = vida_inicial
        self.__veloc_mov = veloc_mov
        self.__veloc_tiro = veloc_tiro

        self.__invencibilidade_cooldown = invic_cooldown
        self.__invencibilidade_temporizador = 0

    @property
    def vida_max(self):
        return self.__vida_max

    @property
    def vida(self):
        return self.__vida

    @property
    def veloc_mov(self):
        return self.__veloc_mov

    @property
    def veloc_tiro(self):
        return self.__veloc_tiro

    def sofrer_dano(self, dano: int):
        if self.__invencibilidade_temporizador >= self.__invencibilidade_cooldown:
            self.__vida -= dano
            self.__invencibilidade_temporizador = 0

        if self.__vida <= 0:
            self.morrer()

    @abstractmethod
    def morrer(self):
        pass

    def update(self, dt):
        self.__invencibilidade_temporizador += dt
