from capacete import Capacete


class CapaceteMilitar(Capacete):
    def __init__(self):
        Capacete.__init__(
            self, 'Capacete Militar', 2, 'Mais armadura, menos velocidade',
            'capacete.png', 1.5, 1
        )

class CapaceteNinja(Capacete):
    def __init__(self):
        Capacete.__init__(
            self, 'Capacete Ninja', 5, 'Mais velocidade, menos armadura',
            'capacete_ninja.png', 1.1, 1.6
        )

class CapaceteBob(Capacete):
    def __init__(self):
        Capacete.__init__(
            self, 'Cabeça Bob', 2, 'Uncle Bob',
            'bob.png', 3, 1.5
        )

class CapaceteTyska(Capacete):
    def __init__(self):
        Capacete.__init__(
            self, 'Cabeça Tyska', 2, 'Uncle Tyska',
            'tyska.png', 2, 2
        )
