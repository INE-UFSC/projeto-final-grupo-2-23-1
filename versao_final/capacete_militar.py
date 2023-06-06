from capacete import Capacete



class CapaceteMilitar(Capacete):
    def __init__(self, velocidade, armadura):
        Capacete.__init__(self, 'Capacete Militar', 2, 'Mais vida, menos velocidade')
        self.__velocidade = velocidade
        self.__armadura = armadura
