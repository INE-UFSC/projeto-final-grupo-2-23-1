from projetil import Projetil

class ProjetilTeleguiado(Projetil):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        super().__init__(dano = dano, veloc_proj = veloc_proj, tamanho = tamanho, perfuracao = perfuracao)
        self.__dano = dano
        self.__veloc_proj = veloc_proj
        self.__tamanho = tamanho
        self.__perfuracao = perfuracao

    def atualizar_trajetoria(self):
        pass


    def sofrer_impacto(self):
        pass

