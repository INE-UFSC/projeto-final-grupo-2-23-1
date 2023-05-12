from acessorio import Acessorio
from projetil import Projetil

class Cajado(Acessorio):
    def __init__(self, nome, custo, descricao, tipo_projetil: Projetil):
        super().__init__(nome, custo, descricao)
        self.__tipo_projetil = tipo_projetil

    def atirar_projetil(self, angulo: float):
        pass
