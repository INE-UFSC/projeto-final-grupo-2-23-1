from abc import ABC, abstractmethod

class Acessorio(ABC):
    def __init__(self, nome, custo, descricao):
        self.__nome = nome
        self.__custo = custo
        self.__descricao = descricao

    @abstractmethod
    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    @property
    def custo(self):
        return self.__custo
    
    @abstractmethod
    @property
    def descricao(self):
        return self.__descricao

    