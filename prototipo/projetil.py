from abc import ABC, abstractmethod


class Projetil(ABC):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__perfuracao = perfuracao

    @abstractmethod
    @property
    def dano(self):
        return self.__dano
    
    @abstractmethod
    @property
    def veloc_proj(self):
        return self.__veloc_proj
    
    @abstractmethod
    @property
    def tamanho(self):
        return self.__tamanho
    
    @abstractmethod
    @property
    def perfuracao(self):
        return self.__perfuracao
    
    

    @abstractmethod
    def atualizar_trajetoria(self):
        pass

    @abstractmethod
    def sofrer_impacto(self):
        pass


    

