

class Inventario:
    def __init__(self):
        self.__espaco_interno = {}

    @property
    def espaco_interno(self):
        return self.__espaco_interno

    @espaco_interno.setter
    def espaco_interno(self, classe):
        