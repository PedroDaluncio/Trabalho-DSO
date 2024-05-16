from outras_classes.Arremesavel import Arremesavel
from outras_classes.Consumivel import Consumivel
from outras_classes.equipavel import Equipavel


class Inventario:
    def __init__(self):
        self.__espaco_interno = {Arremesavel: [],
                                 Consumivel: [],
                                 Equipavel: []}

    @property
    def espaco_interno(self):
        return self.__espaco_interno

    @espaco_interno.setter
    def espaco_interno(self, parametros):
        classe , item = parametros
        self.__espaco_interno[classe].append(item)
