from persistencia.dao import DAO
from entidade.Sessao import Sessao


class SessaoDAO(DAO):
    def __init__(self):
        super().__init__("sessoes.pkl")

    def add(self, sessao: Sessao, **kwargs):
        if isinstance(sessao, Sessao):
            super().add(sessao.data, sessao)

    def remove(self, sessao: Sessao):
        if isinstance(sessao, Sessao):
            self.remove(sessao.data)

    def listagem(self):
        lista = []
        for sessao in super().get_all():
            lista.append([sessao.data, sessao.lista_jogadores, sessao.personagens_participantes])

    def seleciona_um(self, chave):
        for sessao in super().get_all():
            if chave == sessao.data:
                return sessao
