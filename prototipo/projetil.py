from abc import ABC, abstractmethod


class Projetil(ABC):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__perfuracao = perfuracao

    @property
    def dano(self):
        return self.__dano
    
    @property
    def veloc_proj(self):
        return self.__veloc_proj
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def perfuracao(self):
        return self.__perfuracao
