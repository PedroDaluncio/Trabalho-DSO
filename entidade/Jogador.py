from entidade.Personagem import Personagem


class Jogador:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
        self.__personagens = {}

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

    @personagens.setter
    def personagens(self, personagem):
        if isinstance(personagem, Personagem):
            self.__personagens[personagem.nome] = personagem
