from entidade import *

class Inimigo(Entidade):
    def __init__(self, vida_inicial, veloc_mov, veloc_tiro):
        super().__init__(vida_inicial, veloc_mov, veloc_tiro)

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def atirar(self):
        pass 
    