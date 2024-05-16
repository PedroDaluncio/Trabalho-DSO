from entidade.jogador import Jogador
from entidade.personagem import Personagem
import datetime


class Sessao:
    def __init__(self, data: datetime, lista_jogadores: Jogador, personagens_participantes: Personagem):
        self.__jogadores = []
        self.__personagens_participantes = []
        if isinstance(data, datetime.datetime):
            self.__data = data
        if isinstance(lista_jogadores, Jogador):
            self.__jogadores.append(lista_jogadores)
        if isinstance(personagens_participantes, Personagem):
            self.__personagens_participantes.append(personagens_participantes)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, datetime.datetime):
            self.__data = data

    @property
    def lista_jogadores(self):
        return self.__jogadores

    @lista_jogadores.setter
    def lista_jogadores(self, jogadores):
        if isinstance(jogadores, Jogador):
            self.__jogadores.append(jogadores)

    @property
    def personagens_participantes(self):
        return self.__personagens_participantes

    @personagens_participantes.setter
    def personagens_participantes(self, personagens):
        if isinstance(personagens, Personagem):
            self.__personagens_participantes.append(personagens)
