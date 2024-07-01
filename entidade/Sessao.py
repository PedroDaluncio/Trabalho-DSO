from entidade.Jogador import Jogador
from entidade.Personagem import Personagem
import datetime


class Sessao:
    def __init__(self, data, jogadores: list, personagens_participantes: list):
        self.__jogadores = jogadores
        self.__personagens_participantes = personagens_participantes
        self.__data = data
        if isinstance(jogadores, list):
            self.__jogadores = jogadores
        if isinstance(personagens_participantes, list):
            self.__personagens_participantes = personagens_participantes

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def lista_jogadores(self):
        return self.__jogadores

    @lista_jogadores.setter
    def lista_jogadores(self, jogadores):
        self.__jogadores = jogadores

    @property
    def personagens_participantes(self):
        return self.__personagens_participantes

    @personagens_participantes.setter
    def personagens_participantes(self, personagens):
        self.__personagens_participantes = personagens
