from item import Item


class Consumivel(Item):

    def __init__(self, duracao: int, nome: str,
                 valor: int, efeito: str, dano: int):
        super().__init__(nome, valor, efeito, dano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: int):
        if isinstance(duracao, int):
            self.__duracao = duracao
