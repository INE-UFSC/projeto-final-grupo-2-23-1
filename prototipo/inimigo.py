from entidade import *

class Inimigo(Entidade):
    def __init__(self, vida_inicial, veloc_mov, veloc_tiro):
        super().__init__(vida_inicial = vida_inicial, veloc_mov = veloc_mov, veloc_tiro = veloc_tiro)
        self.__vida_inicial = vida_inicial
        self.__veloc_mov = veloc_mov
        self.__veloc_tiro = veloc_tiro

    @property
    def vida_inicial(self):
        return self.__vida_inicial
    
    @property
    def veloc_mov(self):
        return self.__veloc_mov
    
    @property
    def veloc_tiro(self):
        return self.__veloc_tiro
    
    @abstractmethod
    def sofrer_dano(self, dano: int):
        self.__dano = self.__dano - dano

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def atirar(self):
        pass 

    

    