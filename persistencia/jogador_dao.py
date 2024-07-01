from persistencia.dao import DAO
from entidade.Jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__("jogadores.pkl")

    def add(self, jogador: Jogador, **kwargs):
        if isinstance(jogador, Jogador):
            super().add(jogador.nome, jogador)

    def remove(self, jogador: str):
        if isinstance(jogador, str):
            super().remove(jogador)

    def listagem(self):
        lista = []
        for jogador in super().get_all():
            lista.append([jogador.nome, jogador.idade])
        return lista

    def seleciona_um(self, chave):
        for jogador in super().get_all():
            if chave == jogador.nome:
                return jogador
