from abc import ABC, abstractmethod


class Entidade(ABC):
    def __init__(self, vida_inicial: int, veloc_mov: float, veloc_tiro: float):
        self.__vida = vida_inicial
        self.__veloc_mov = veloc_mov
        self.__veloc_tiro = veloc_tiro

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
        self.__vida -= dano

        if self.__vida <= 0:
            self.morrer()

    @abstractmethod
    def morrer(self):
        pass
