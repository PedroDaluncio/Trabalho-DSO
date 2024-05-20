from outras_classes.Arremesavel import Arremesavel
from outras_classes.Consumivel import Consumivel
from outras_classes.Equipavel import Equipavel


class Inventario:
    def __init__(self):
        self.__espaco_interno = {}
        self.__itens_adquiridos = {}
        self.__itens_perdidos = {}
        self.__personagem = ''

    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem):
        self.__personagem = personagem

    @property
    def espaco_interno(self):
        return self.__espaco_interno[self.__personagem]

    @espaco_interno.setter
    def espaco_interno(self, parametros):
        classe, item = parametros
        self.__espaco_interno[self.__personagem][classe].append(item)

    @property
    def itens_adquiridos(self):
        return self.__itens_adquiridos

    @itens_adquiridos.setter
    def itens_adquiridos(self, item):
        if self.__personagem in self.__itens_adquiridos and self.__itens_adquiridos[self.__personagem]:
            self.__itens_adquiridos[self.__personagem].append(item)
        else:
            self.__itens_adquiridos[self.__personagem] = []
            self.__itens_adquiridos[self.__personagem].append(item)

    @property
    def itens_perdidos(self):
        return self.__itens_perdidos

    @itens_perdidos.setter
    def itens_perdidos(self, item):
        self.__itens_perdidos[self.__personagem].append(item)

    def cria_inventario(self, personagem, inventario):
        self.__espaco_interno[personagem] = inventario
        self.__itens_adquiridos[personagem] = []
        self.__itens_perdidos[personagem] = []
