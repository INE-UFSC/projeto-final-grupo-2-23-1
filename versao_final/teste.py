class Teste:
    def __init__(self):
        self.__pulo= 70

    @property
    def pulo(self):
        return self.__pulo

    @pulo.setter
    def pulo(self, valor):
        self.__pulo = valor

teste = Teste()
print(teste.pulo)
teste.pulo = 90
print(teste.pulo)