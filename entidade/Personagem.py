

class Personagem():
    def __init__(self, nome, nivel, classe, raca):
        self.__nome = nome
        self.__nivel = nivel
        self.__classe = classe
        self.__raca = raca
        self.__qt_niveis_adquiridos = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, classe):
        self.__classe = classe

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def qt_niveis_adquiridos(self):
        return self.__qt_niveis_adquiridos

    @qt_niveis_adquiridos.setter
    def qt_niveis_adquiridos(self, qt_niveis):
        self.__qt_niveis_adquiridos = qt_niveis
