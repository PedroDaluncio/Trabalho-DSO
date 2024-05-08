from item import Item


class Arremesavel(Item):

    def __init__(self, alcance: float, nome: str,
                 valor: int, efeito: str, dano: int):
        super().__init__(nome, valor, efeito, dano)
        self.__alcance = alcance

    @property
    def alcance(self):
        return self.__alcance

    @alcance.setter
    def alcance(self, alcance: float):
        if isinstance(alcance, float):
            self.__alcance = alcance
