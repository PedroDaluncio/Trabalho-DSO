from persistencia.dao import DAO
from entidade.Jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__("jogadores.pkl")

    def add(self, jogador: Jogador, **kwargs):
        if isinstance(jogador, Jogador):
            super().add(jogador.nome, jogador)

    def remove(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            self.remove(jogador.nome)
