from projetil import Projetil, ProjetilConcreto
from projetil_trajetorias import trajetoria_linear


class ProjetilLinear(Projetil):
    def __init__(self, dano: int, veloc_proj: float, tamanho: float, cor):
        Projetil.__init__(self, dano, veloc_proj, tamanho, cor)

    def criar_projetil(self, pos, angulo):
        proj = ProjetilConcreto(
            self.dano, self.veloc_proj, self.tamanho, self.cor, trajetoria_linear, pos, angulo
        )

        return proj
