from outras_classes.Arremesavel import Arremesavel
from outras_classes.Consumivel import Consumivel
from outras_classes.equipavel import Equipavel


class Inventario:
    def __init__(self):
        self.__espaco_interno = {Arremesavel: [],
                                 Consumivel: [],
                                 Equipavel: []}
        self.__itens_adquiridos = []
        self.__itens_perdidos = []

    @property
    def espaco_interno(self):
        return self.__espaco_interno

    @espaco_interno.setter
    def espaco_interno(self, parametros):
        classe , item = parametros
        self.__espaco_interno[classe].append(item)

    @property
    def itens_adquiridos(self):
        return self.__itens_adquiridos

    @itens_adquiridos.setter
    def itens_adquiridos(self, item):
        self.__itens_adquiridos.append(item)

    @property
    def itens_perdidos(self):
        return self.__itens_perdidos

    @itens_perdidos.setter
    def itens_perdidos(self, item):
        self.__itens_perdidos.remove(item)
