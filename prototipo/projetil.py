from abc import ABC, abstractmethod


class Projetil(ABC):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__perfuracao = perfuracao

    @abstractmethod
    def atualizar_trajetoria(self):
        pass

    @abstractmethod
    def sofrer_impacto(self):
        pass


    

