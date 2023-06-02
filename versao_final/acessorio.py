from abc import ABC


class Acessorio(ABC):
    def __init__(self, nome, custo, descricao):
        self.__nome = nome
        self.__custo = custo
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def custo(self):
        return self.__custo

    @property
    def descricao(self):
        return self.__descricao
