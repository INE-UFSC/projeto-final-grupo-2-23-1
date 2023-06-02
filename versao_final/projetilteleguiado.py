from projetil import Projetil

class ProjetilTeleguiado(Projetil):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, perfuracao: int):
        super().__init__(dano, veloc_proj, tamanho, perfuracao)

    def atualizar_trajetoria(self):
        pass


    def sofrer_impacto(self):
        pass

