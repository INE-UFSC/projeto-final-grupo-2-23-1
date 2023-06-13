from capacete import Capacete



class CapaceteMilitar(Capacete):
    def __init__(self):
        Capacete.__init__(self, 'Capacete Militar', 2, 'Mais vida, menos velocidade')
        self.__velocidade = 1.5
        self.__armadura = 0.8


