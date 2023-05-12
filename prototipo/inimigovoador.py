from inimigo import Inimigo

class InimigoVoador(Inimigo):
    def __init__(self, vida_inicial, veloc_mov, veloc_tiro):
        super().__init__(vida_inicial, veloc_mov, veloc_tiro)

        