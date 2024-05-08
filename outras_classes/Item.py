from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def __init__(self, nome: str, valor: int, efeito: str, dano: int):
        self.__nome = nome
        self.__valor = valor
        self.__efeito = efeito
        self.__dano = dano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: int):
        if isinstance(valor, int):
            self.__valor = valor

    @property
    def efeito(self):
        return self.__efeito

    @efeito.setter
    def efeito(self, efeito: str):
        if isinstance(efeito, str):
            self.__efeito = efeito

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self, dano: int):
        if isinstance(dano, int):
            self.__dano = dano
