from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, vida_inicial: int, veloc_mov: float, veloc_tiro: float):
        self.__vida_inicial = vida_inicial
        self.__veloc_mov = veloc_mov
        self.__veloc_tiro = veloc_tiro

    @abstractmethod
    @property
    def vida_inicial(self):
        return self.__vida_inicial
    
    @abstractmethod
    @property
    def veloc_mov(self):
        return self.__veloc_mov
    
    @abstractmethod
    @property
    def veloc_tiro(self):
        return self.__veloc_tiro
    
    @abstractmethod
    def sofrer_dano(self, dano: int):
        self.__dano = self.__dano - dano

    @abstractmethod
    def morrer(self):
        pass


        
