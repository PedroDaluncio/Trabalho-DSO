from outras_classes.item import Item


class Equipavel(Item):

    def __init__(self, nome: str, valor: int, efeito: str,
                 dano: int, durabilidade: int):
        super().__init__(nome, valor, efeito, dano)
        self.__durabilidade = durabilidade

    @property
    def durabilidade(self):
        return self.__durabilidade

    @durabilidade.setter
    def durabilidade(self, durabilidade: int):
        if isinstance(durabilidade, int):
            self.__durabilidade = durabilidade
