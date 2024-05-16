

class Jogador:
    def __init__(self, nome: str, idade: int, personagens: dict):
        self.__nome = nome
        self.__idade = idade
        self.__personagens = personagens

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def personagens(self):
        return self.__personagens
